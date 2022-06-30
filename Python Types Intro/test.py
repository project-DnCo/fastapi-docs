from typing import List, Set, Tuple


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
