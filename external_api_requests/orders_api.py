import json
from typing import List, Dict

from consts import *
from models.models import Order


class OrdersAPI:

    def __init__(self):
        self.json_file = open(JSON_PATH)

    def get_json_data(self):
        data = json.load(self.json_file)

        return data

    def get_orders_from_json(self, json_data: Dict) -> List[Order]:
        orders = []

        for order in json_data.get('orders'):
            orders.append(
                Order(
                    customer_name=order.get('customer_name'),
                    time=order.get('time'),
                    address=order.get('address'),
                    comments=order.get('comments')
                )
            )

        self.json_file.close()

        return orders

    def add_order_to_json(self, customer_name: str, time: str, address: str, comments: str) -> List[Order]:
        orders_data = self.get_orders_from_json(self.get_json_data())

        orders_data.append(
                Order(
                    customer_name=customer_name,
                    time=time,
                    address=address,
                    comments=comments
                )
            )

        return orders_data

