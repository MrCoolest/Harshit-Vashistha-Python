# Using getter & setter decorater

class Phone:
    def __init__(self, Brand, model, price):
        # instance variables
        self.brand = Brand
        self.model = model
        self._price  = max(price,0)
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
         # self.Compelete_specification = f"{self.brand} {self.model} price is {self._price}"

    @property
    def Compelete_specification(self):
        return f"{self.brand} {self.model} price is {self._price}"

    # getter and setter decoratera
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
        

    def make_a_call(self,number):
        print(f"Calling {number}")

    def full_name(self):
        return f"{self.brand} {self.model}"


phone1 = Phone('INFINIX','HOT 7 PRO', 10000)
print(phone1.brand)
print(phone1.model)
phone1.price = -5000
print(phone1.price)
print(phone1.Compelete_specification)      
