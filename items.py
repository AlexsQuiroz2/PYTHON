'''item1 = "Phone"
items_price = 100
items_quantity = 5
items_total_price = items_price * items_quantity

print(type(item1)) # str
print(type(items_price)) # int
print(type(items_quantity)) # int
print(type(items_total_price)) # int '''


class item:
    def __init__(self, name, price, quantity=0):
         print("An instance created: {name}")
         self.name = name 
         self.price = price
         self.quantity = quantity
    
    def calculate_total_price(self):
         return self.price * self.quantity

item1 = item("phone", 100, 1)
'''item1.name = "Phone"'''
'''item1.price = 100'''
'''item1.quantity = 5'''
'''item1.calculate_total_price(item1.price, item1.quantity)
print(item1.calculate_total_price(item1.price, item1.quantity))'''
    
item2 = item("laptop", 1000, 3)
'''item2.name = "Laptop"'''
'''item2.price = 1000
item2.quantity = 3'''
'''print(item2.calculate_total_price(item2.price, item2.quantiy))'''

print(item1.calculate_total_price())
print(item2.calculate_total_price())



'''print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)'''
'''print(item1.quantity)
print(item2.quantity)'''




