# change class variable
# use slef.variable instide of class name to give self dicount

class Laptop:
    disco = 10
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def dicount(self):
        a = (self.disco/100)*self.price
        return self.price - a

s = Laptop('Dell','Xyz',70000)
s.disco = 50

print(s.__dict__)
print(s.dicount())