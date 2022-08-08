'''item1 = "Phone"
items_price = 100
items_quantity = 5
items_total_price = items_price * items_quantity

print(type(item1)) # str
print(type(items_price)) # int
print(type(items_quantity)) # int
print(type(items_total_price)) # int '''


class item:
    def calculate_total_price(self, x, y):
         return x * y

item1 = item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
item1.calculate_total_price(item1.price, item1.quantity)
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3


 




