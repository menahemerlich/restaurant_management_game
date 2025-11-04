
class Menultem:
    def __init__(self, name, price, category, available = True):
        self.name = name
        self.price = price
        self.category = category
        self.available = available

    def get_info(self):
        print(f"name: {self.name}, price: {self.price}, category: {self.category}")

    def set_available(self, status):
        self.available = status

    def is_available(self):
        if self.available:
            return True
        return False



