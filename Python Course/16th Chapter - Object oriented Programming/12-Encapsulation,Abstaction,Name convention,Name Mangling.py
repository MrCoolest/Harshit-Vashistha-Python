# Encapsulation
# Abstraction
# Some special Name convention
# Name mangling
# _name is convention to private property
# __name__ dunder/magic method
class Phone:
    def __init__(self, brand_name, model_name, price):
        # instance Variable
        self.brand = brand_name
        self.model = model_name
        self.__price = price

    def Make_a_call(self,number):
        print(f'Calling {number}')

    def full_name(self):
        return f'{self.brand} {self.model}'

             

phone1 = Phone('INFINX','HOT 7 PRO',9999)
print(phone1.full_name()) 
Phone.Make_a_call(8291351,231)
print(phone1.__dict__)
print(phone1._Phone__price)
phone1._Phone__price = 100000
print(phone1._Phone__price)