from classes.customer import Customer
from classes.order import Order
from classes.menu_item import Menu_item

item1 = Menu_item("banana", 10, "food")
item2 = Menu_item("appel", 5, "food")
cost1 = Customer("Avi")
ord1 = Order(cost1, 1)
ord1.add_item(item1)
ord1.add_item(item2)
ord1.display_order()
ord1.set_status("cooking")
ord1.display_order()




