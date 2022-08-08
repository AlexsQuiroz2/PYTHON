'''item1 = "Phone"
items_price = 100
items_quantity = 5
items_total_price = items_price * items_quantity

print(type(item1)) # str
print(type(items_price)) # int
print(type(items_quantity)) # int
print(type(items_total_price)) # int '''


class item:
    pay_rate = 0.8 #The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):        
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        
        self.name = name 
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
         return self.price * self.quantity
     
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = item("phone", 100, 1) 
item1.apply_discount()
print(item1.price)

item2 = item("laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


