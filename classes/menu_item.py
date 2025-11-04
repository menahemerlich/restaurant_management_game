
class Menu_item:
    def __init__(self, name: str, price: float, category: str, available: bool = True):
        self.name = name
        self.price = price
        self.category = category
        self.available = available

    def get_info(self):
        return f"name: {self.name}, price: {self.price}, category: {self.category}"

    def set_available(self, status: bool):
        self.available = status

    def is_available(self):
        if self.available:
            return True
        return False



