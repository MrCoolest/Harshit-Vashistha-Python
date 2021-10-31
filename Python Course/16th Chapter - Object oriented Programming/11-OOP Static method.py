# STATIC METHOD
class Person:
    count = 0 #class variable / class methods 
    def __init__(self, name, last, age):
        Person.count += 1
        # INSTANCE VARAIBLE
        self.name = name
        self.last = last
        self.age = age

    @classmethod
    def from_string(cls,string):
        name,last,age = string.split(',')
        return cls(name,last,age)

    @staticmethod
    def hello():
        print('Hello, its Ankit, You are calling static method')


    @classmethod
    def counts(cls):
        return f'You have created {cls.count} of {cls.__name__}'    

    def full_name(self):
        return f'{self.name} {self.last}'

    def Check_adult(self):
        return self.age > 18


p1 = Person('Ankit','Patwa',19)
p2 = Person('Yash','Kadam',20)

Person.hello()