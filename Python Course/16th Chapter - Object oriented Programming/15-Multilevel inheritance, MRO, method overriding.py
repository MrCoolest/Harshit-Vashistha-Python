# can we derived more than one class from base class? >>>> yes
# MULtilevel inheritance
# method resolution order
# method overridiing
# isinstance(), issubclass()

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
        self.rom = Rom
        self.ram = Ram
        self.Camera = Camera

    def full_name(self):  #method overriding
        return f"{self.brand} {self.model} and ROM is {self.rom}, RAM is {self.ram} "    

class Flagshipphone(SmartPhone): #this is Multilevel inheritance
    def __init__(self, brand, model, price, Rom, Ram, Camera, Front_cam):
        super().__init__(brand, model, price,Rom,Ram,Camera)
        self.front = Front_cam
    
    def full_name(self): #method overriding
        return f"{self.brand} {self.model} and ROM is {self.rom}, RAM is {self.ram}, Cam {self.Camera}, front is {self.front} "

Phone1 = Phone('JIO',"xyz", 1000)
Mobile1 = SmartPhone('Infinix', 'hot 7 pro', 10000, '64gb','6gb','13+2 mp')

print(Phone1.full_name())
print(Mobile1.full_name())

Mobile2 = Flagshipphone('Infinix', 'hot 7 pro', 10000, '64gb','6gb','13+2 mp', '12 mp')
print(Mobile2.full_name())
# print(help(Flagshipphone)) # method resolution order

print(isinstance(Mobile1,Phone)) #isinstance
print(issubclass(Flagshipphone, SmartPhone)) #issubclass 