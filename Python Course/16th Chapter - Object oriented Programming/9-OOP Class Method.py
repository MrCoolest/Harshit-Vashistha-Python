# CLASS METHOD 
class Person:
    count = 0 #class variable / class methods 
    def __init__(self, name, last, age):
        Person.count += 1
        # INSTANCE VARAIBLE
        self.name = name
        self.last = last
        self.age = age

    @classmethod
    def counts(cls):
        return f'You have created {cls.count} of {cls.__name__}'    

    def full_name(self):
        return f'{self.name} {self.last}'

    def Check_adult(self):
        return self.age > 18


p1 = Person('Ankit','Patwa',19)
p2 = Person('Yash','Kadam',20)
print(p1.full_name())
print(p2.Check_adult()) #instance method
print(Person.counts()) #class method 
print(Person.count) #class variable