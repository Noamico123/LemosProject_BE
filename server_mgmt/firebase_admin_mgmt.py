from typing import List, Dict, Optional

import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import firestore

from consts import CREDS
from external_api_requests.orders_api import OrdersAPI
from external_api_requests.printnode_api import PrintNodeAPI
from models.models import User, Order


class FirebaseMGMT:

    def __init__(self):

        if not firebase_admin._apps:
            self.cred = credentials.Certificate(CREDS)
            self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    @staticmethod
    def get_users_from_auth() -> List[User]:
        page = auth.list_users()
        users = []

        for user in page.users:
            users.append(User(
                is_admin='true' if user.email == 'noam@ggg.com' else 'false',
                user_name=user.email,
                uid=user.uid,
                printers=[],
                orders=[],
                api_key=''
            ))

        return users

    def get_users_from_storage(self) -> List[User]:
        users_data_list = []
        doc_ref = self.db.collection(u'Users')

        docs = doc_ref.get()

        for user in docs:
            user_dict = user.to_dict()
            users_data_list.append(user_dict)

        return users_data_list

    def post_user(self, email, api_key, is_admin) -> List:
        users_data_list_objects = self.get_users_from_storage()
        users_data_list = []

        users_data_list_objects.append(User(
            is_admin=is_admin,
            user_name=email,
            printers=[],
            orders=[],
            api_key=api_key)
        )
        new_user = auth.create_user(email=email)

        for user in users_data_list_objects:
            if type(user) is not dict:
                user = user.__dict__
            users_data_list.append(user)

            if user.get('uid') is None and user.get('user_name') == email:
                user['uid'] = new_user.uid

            self.db.collection(u'Users').document(user.get('uid')).set(user)

        return users_data_list

    def post_users(self) -> List:
        users_data_list_objects = self.get_users_from_auth()
        users_data_list = []

        for user in users_data_list_objects:
            user_dic = user.__dict__
            users_data_list.append(user_dic)

            self.db.collection(u'Users').document(user_dic.get('uid')).set(user_dic)

        return users_data_list

    def update_user(self, email: str, is_admin: str) -> List:
        users_data_list_objects = self.get_users_from_auth()
        users_data_list = []

        for user in users_data_list_objects:
            user_dic = user.__dict__
            users_data_list.append(user_dic)

            if user_dic.get('user_name') == email:
                user_dic['is_admin'] = is_admin

            self.db.collection(u'Users').document(user_dic.get('uid')).set(user_dic)
            print(user_dic)
        return users_data_list

    def get_printers(self) -> List:

        printers_data_list = []
        doc_ref = self.db.collection(u'Printers')

        docs = doc_ref.get()

        for printer in docs:
            printer_dict = printer.to_dict()
            printers_data_list.append(printer_dict)

        return printers_data_list

    def post_printers(self) -> List:

        # getting data from printnode api
        print_node_api = PrintNodeAPI()
        res_json = print_node_api.get_printers_data_from_printnode_api()

        printers_data = print_node_api.get_printers_list(res_json)

        printers_data_list = []

        for printer in printers_data:
            printer_dic = printer.__dict__
            printers_data_list.append(printer_dic)

            self.db.collection(u'Printers').document(printer_dic.get('id')).set(printer_dic)

        return printers_data_list

    def update_printer_nickname(self, printer_id: str, printer_name: str) -> List:
        printers_data_list = self.get_printers()

        for printer in printers_data_list:
            if printer.get('id') == printer_id:
                printer['nickname'] = printer_name

            self.db.collection(u'Printers').document(printer.get('id')).set(printer)

        return printers_data_list

    def update_printer_state(self, printer_id: str, printer_state: str) -> List:
        printers_data_list = self.get_printers()

        for printer in printers_data_list:
            if printer.get('id') == printer_id:
                printer['state'] = printer_state

            self.db.collection(u'Printers').document(printer.get('id')).set(printer)

        return printers_data_list

    def get_orders(self) -> List:
        orders_data_list = []
        doc_ref = self.db.collection(u'Orders')

        docs = doc_ref.get()

        for order in docs:
            order_dict = order.to_dict()
            orders_data_list.append(order_dict)

        return orders_data_list

    def post_orders(self, orders_data: Optional[List[Order]] = None) -> List:

        if orders_data is None:
            orders_data_api = OrdersAPI()
            orders_data = orders_data_api.get_orders_from_json(orders_data_api.get_json_data())

        orders_data_list = []

        for order in orders_data:
            order_dict = order.__dict__
            orders_data_list.append(order_dict)

            self.db.collection(u'Orders').document(order_dict.get('id')).set(order_dict)

        return orders_data_list

    def add_order_to_json(self, customer_name: str, time: str, address: str, comments: str) -> Dict:
        order = Order(
            customer_name=customer_name,
            time=time,
            address=address,
            comments=comments
        )

        order_dict = order.__dict__

        self.db.collection(u'Orders').document(order_dict.get('id')).set(order_dict)

        return order_dict
