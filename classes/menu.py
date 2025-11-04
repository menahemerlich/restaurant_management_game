from itertools import count

from classes.menu_item import Menu_item

class Menu:
    def __init__(self, items: list):
        self.items = items
        self.menu_item = None

    def add_item(self, menu_item: Menu_item):
        self.items.append(menu_item)

    def remove_item(self, item_name: str):
        count = 0
        for item in self.items:
            if item.name == item_name:
                self.items.pop(count)
            count += 1

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return "not found."

    def get_items_by_category(self, category):
        return_list = []
        for item in self.items:
            if item.category == category:
                return_list.append(item)
        return return_list

    def display_menu(self):
        print("~-~ available items ~-~")
        count = 1
        for item in self.items:
            if item.available:
                print(f"    {count}. {item.name}")
                count += 1

    def get_total_items(self):
        count = 0
        for item in self.items:
            count += 1
        return count

