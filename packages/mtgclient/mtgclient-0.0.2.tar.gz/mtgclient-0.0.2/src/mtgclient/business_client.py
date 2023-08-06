from typing import Tuple, List

from requests import request as req

url_db = 'http://www.google.ru'

responce = req(method='GET', url=url_db)


class Categories:
    def __init__(self):
        # connect to db
        pass

    def get_categories(self):
        categories = ['Сигареты', 'Табак', 'Калик', 'Электронки']
        return categories

    def get_subcategories(self, category: str) -> List:
        # get from db
        test_dict = {
            'Сигареты': ['Parlament', 'Huyament', 'Winston', 'Huinstom'],
            'Табак': ['Odin', 'Vtoroy'],
            'Калик': ['Huyarik', 'Muyarik'],
            'Электронки': ['Disepticon', 'Jili byily', 'Sosna']
        }
        return test_dict[category]

    def subcategory_exist(self) -> bool:
        return True


class Items:
    def __init__(self) -> None:
        # connect to db (creds, url)
        self.position = 0
        self.items = []

    def _moving_descriptor(self, move: str, current_position: int, data_len: int) -> int:
        new_position = 0
        data_len = data_len - 1
        if move.lower() == 'left':
            new_position = data_len if current_position == 0 else current_position - 1
        elif move.lower() == 'right':
            new_position = 0 if current_position == data_len else current_position + 1
        return new_position

    def get_items(self, move: str = None) -> Tuple[str, int, int]:
        # connection object
        # get data by category
        if move is not None:
            self.position = self._moving_descriptor(move, self.position, len(self.items))
        return self.items[self.position], (self.position + 1), len(self.items)

    def get_items_by_category(self, category: str) -> None:
        media_url = [
            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Snake_River_%285mb%29.jpg/2560px-Snake_River_%285mb%29.jpg',
            'https://i.stack.imgur.com/f5f0L.png',
            'https://webtous.ru/wp-content/uploads/2019/04/foto-test.jpg']
        self.items = media_url


class Post:
    Name: str
    Description: str
    Price: float
    Photo: str


class Item:
    def __init__(self):
        pass

    @property
    def name(self):
        pass

    @property
    def description(self):
        pass

    @property
    def characteristics(self):
        pass

    @property
    def cost(self):
        pass


class Range:
    # List of items (Ассортимент)
    def __init__(self):
        pass

    def add_item(self):
        pass

    def update_item(self):
        # particialy!!!
        pass

    def delete_item(self):
        pass

    def items_list(self):
        pass


class Basket:
    def __init__(self):
        pass

    def add_item(self):
        pass

    def delete_item(self):
        pass

    def items_list(self):
        pass


class Users:
    def __init__(self):
        pass

    @property
    def user_name(self):
        pass

    @property
    def password(self):
        pass

    def create_user(self):
        pass

    def add_user(self):
        pass

    def delete_user(self):
        pass


class Workers:
    def __init__(self):
        pass

    @property
    def emploee_name(self):
        pass

    @property
    def job_title(self):
        pass

    @property
    def job_description(self):
        pass

    @property
    def job_address(self):
        pass


class BusinessClient:
    def __init__(self):
        pass

    # some logic
    # Connect to db with Item, Range, Basket, Users, Workers
