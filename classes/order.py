from classes.customer import Customer

class Order:
    def __init__(self, customer: Customer, order_number: int):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.total_price += menu_item.price

    def remove_item(self, menu_item):
        count = 0
        for item in self.items:
            if item == menu_item:
                self.items.pop(count)
                self.total_price -= menu_item.price
            count += 1

    def get_total(self):
        return self.total_price

    def set_status(self, new_status: str):
        status_list = ["pending", "cooking", "ready","delivered"]
        if new_status in status_list:
            self.status = new_status
        else:
            print("Error status!")

    def display_order(self):
        print(f"order num.: {self.order_number}\n"
              f"customer name: {self.customer.name}\n"
              f"items: {[self.items[i].name for i in range(len(self.items))]}\n"
              f"price: {self.total_price}\n"
              f"order status: {self.status}")

    def is_complete(self):
        if self.status == "delivered":
            return True
        return False





