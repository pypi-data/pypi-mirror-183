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
    