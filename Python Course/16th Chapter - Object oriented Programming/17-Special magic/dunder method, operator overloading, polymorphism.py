# Special magic method / dunder method
# opertor overloading
# polymorphism  / Method overriding is called as polymorphism

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price   

    def Phone_name(self):
        return f'{self.brand} {self.model}'

    #__str__ , __repr__
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\',\'{self.model}\',\'{self.price}\')' 

    def __len__(self):
        return len(self.Phone_name())

    def __len__(self):
        return len(self.__str__())

    # Operators over loading 
    def __add__(self,other):
        return self.price + other.price

    def __mul__ (self,other):
        return self.price * other.price

class Smartphone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def Phone_name(self):
        return f'{self.brand} {self.model}  and price is {self.price}'    
        
    def __len__(self):
        return len(self.Phone_name())

Phone1 = Phone('Nokia','1100',1000)
Phone2 = Phone('Nokia','1600',1200)
Smart1 =Smartphone('INFINX', 'HOT 7 PRO', 10000,'15 MP')
print(Phone1.Phone_name())
print(Smart1.Phone_name())
print(len(Smart1))
print(Phone1) #__str__   
print(Phone1.__repr__())
print(len(Phone1))
print(Phone1 + Phone2)
print(Phone1 * Phone2)