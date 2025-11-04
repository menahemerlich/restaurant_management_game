from classes.menu_item import Menu_item
from classes.menu import Menu

m1 = Menu_item("a", 10, "food")
m2 = Menu_item("b", 10, "food")
m3 = Menu_item("c", 10, "fooad")
m = Menu(items = [])
m.add_item(m1)
m.add_item(m2)
m.add_item(m3)
print(len(m.items))
m.remove_item("a")
print(len(m.items))
f = m.get_item_by_name("a")
ff = m.get_items_by_category("food")
print(len(ff))
m.display_menu()
print(m.get_total_items())



