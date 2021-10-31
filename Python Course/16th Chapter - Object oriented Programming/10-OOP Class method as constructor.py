# How we create our constructor as class method
# CLASS METHOD 
class Person:
    count = 0 #class variable / class methods 
    def __init__(self, name, last, age):
        Person.count += 1
        # INSTANCE VARAIBLE
        self.name = name
        self.last = last
        self.age = age

    @classmethod #CLASS METHOD AS CONSTRUCTER
    def from_string(cls,string):
        name,last,age = string.split(',')
        return cls(name,last,age)


    @classmethod
    def counts(cls):
        return f'You have created {cls.count} of {cls.__name__}'    

    def full_name(self):
        return f'{self.name} {self.last}'

    def Check_adult(self):
        return self.age > 18


p1 = Person('Ankit','Patwa',19)
p2 = Person('Yash','Kadam',20)

p3=Person.from_string('Ankit,Patwa,19') #CALLING CLASS METHOD AS CONSTRUCTOR
print(p3.name)
print(p3.last)
print(p3.age)
