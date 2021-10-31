# 2nd exercise

class Laptop:
    def __init__(self,name,model,price):
        # instance variable
        self.name = name
        self.model = model
        self.price = price

    def discout(self,a):
        P = (a/100)*self.price
        return self.price - P


p1 = Laptop('Dell','XYZ',90000)
print(p1.discout(10))