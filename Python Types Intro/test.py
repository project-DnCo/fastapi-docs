from pydantic import BaseModel
from datetime import datetime
from typing import List, Set, Tuple, Dict, Union, Optional


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


def process_items1(items: List[str]):
    for item in items:
        print(item)


def process_items2(items: list[str]):
    for item in items:
        print(item)


def process_items3(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s


def process_items4(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items5(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_items6(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item7(item: Union[int, str]):
    print(item)


def process_item8(item: int | str):
    print(item)


def say_hi1(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


def say_hi2(name: Union[str, None] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


def say_hi3(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


def say_hi4(name: Optional[str]):
    print(f"Hey {name}!")


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


class User1(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: List[int] = []


class User2(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []


class User3(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],


}

user1 = User1(**external_data)
print(user1)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user1.id)
# > 123

user2 = User2(**external_data)
print(user2)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user2.id)
# > 123

user3 = User3(**external_data)
print(user3)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user3.id)
# > 123
