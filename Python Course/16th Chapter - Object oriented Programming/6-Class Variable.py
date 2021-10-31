# CLASS VARIABLE

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def circum(self):
        return 2*Circle.pi*self.radius

c =Circle(3)
print(c.circum())            

print(c.radius)

# Example 2
class Laptop:
    Dicso =10
    def __init__(self,name,model,price):
        # instance variable
        self.name = name
        self.model = model
        self.price = price

    def discout(self):
        P = (Laptop.Dicso/100)*self.price
        return self.price - P


p1 = Laptop('Dell','XYZ',90000)
print(p1.discout())