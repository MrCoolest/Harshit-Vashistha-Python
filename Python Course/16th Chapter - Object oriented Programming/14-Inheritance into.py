# INHERITANCE INTRO

class Phone: #base class / parent class
    def __init__(self, brand, model, price):
        # instance variable
        self.brand = brand
        self.model = model 
        self._price = max(price,0)


    def full_name(self):
        return f"{self.brand} {self.model}"

    def make_a_call(self,number):
        return f'Calling {number}....'

class SmartPhone(Phone): #derived class / child class
    def __init__(self, brand, model, price, Rom, Ram, Camera):
        # two ways
        # Phone.__init__(self, brand, model, price) ##uncommon way
        super().__init__(brand, model, price)
        self.ram = Ram
        self.Camera = Camera

Phone1 = Phone('JIO',"xyz", 1000)
Mobile1 = SmartPhone('Infinix', 'hot 7 pro', 10000, '64gb','6gb','13+2 mp')

print(Phone1.full_name())
print(Mobile1.full_name())
