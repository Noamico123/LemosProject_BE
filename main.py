# from typing import Tuple
#
# from dotenv import load_dotenv
# from flask import Flask
#
# from external_api_requests.orders_api import OrdersAPI
# from external_api_requests.printnode_api import PrintNodeAPI
# from server_mgmt.firebase_admin_mgmt import FirebaseMGMT
#
#
# #
# # def init_server() -> Tuple[PrintNodeAPI, OrdersAPI, FirebaseMGMT]:
# #     print_node_api_obj = PrintNodeAPI()
# #     orders_data_api_obj = OrdersAPI()
# #     firebase_db_obj = FirebaseMGMT()
# #
# #     return print_node_api_obj, orders_data_api_obj, firebase_db_obj
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, Lemos!'
#
#
# @app.route('/users')
# def flask_get_users():
#     firebase_db = FirebaseMGMT()
#     users_data = firebase_db.get_users()
#
#     users_data_dict = {}
#
#     for user in users_data:
#         or_dic = user.__dict__
#         users_data_dict[or_dic.get('user_name')] = user
#
#     return dict(users_data_dict)
#
#
# @app.route('/printers', methods=['GET'])
# def flask_get_printers():
#     firebase_db = FirebaseMGMT()
#     printers_data = firebase_db.get_printers()
#
#     print(printers_data)
#     print(type(printers_data))
#
#     return dict({200: printers_data})
#
#
# @app.route('/printers', methods=['POST'])
# def flask_post_printers():
#     firebase_db = FirebaseMGMT()
#     printers_data = firebase_db.post_printers()
#
#     return dict({200: printers_data})
#
#
# @app.route('/orders', methods=['GET'])
# def flask_get_orders():
#     firebase_db = FirebaseMGMT()
#     orders_data = firebase_db.get_orders()
#
#     print(orders_data)
#     print(type(orders_data))
#
#     return dict({200: orders_data})
#
#
# @app.route('/orders', methods=['POST'])
# def flask_post_orders():
#     firebase_db = FirebaseMGMT()
#     orders_data = firebase_db.post_orders()
#
#     return dict({200: orders_data})
#
#
# if __name__ == '__main__':
#
#     load_dotenv()
#     app.run(debug=True, port=8003)

    # print_node_api = PrintNodeAPI()
    # orders_data_api = OrdersAPI()
    # firebase_db = FirebaseMGMT()
    #
    # user_info = print_node_api.get_user_data_from_printnode_api()
    # res_json = print_node_api.get_printers_data_from_printnode_api()
    #
    # printers_data = print_node_api.get_printers_list(res_json)
    # orders_data = orders_data_api.get_orders_from_json(orders_data_api.get_json_data())
    # users_data = firebase_db.get_users()
    #
    # for printer in printers_data:
    #     print(printer)
    #
    # print("\n")
    #
    # for order in orders_data:
    #     print(order)
    #
    # print("\n")
    #
    # for user in users_data:
    #     print(user)




