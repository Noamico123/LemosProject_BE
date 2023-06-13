from dataclasses import dataclass
from typing import List


@dataclass(frozen=False)
class Printer:
    id: str = None
    name: str = None
    nickname: str = None
    state: str = None
    description: str = None
    paper_types: str = None


@dataclass(frozen=False)
class Order:
    customer_name: str = None
    time: str = None
    address: str = None
    comments: str = None


@dataclass(frozen=False)
class User:
    is_admin: str = None
    user_name: str = None
    uid: str = None
    api_key: str = None
    printers: List[Printer] = None
    orders: List[Order] = None

