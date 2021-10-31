class Person:
    classVar = 0
    def __init__(self,name,last,age):
        Person.classVar += 1
        self.name = name
        self.last = last
        self.age = age

p1 = Person('Ankit','Patwa',19)
p2 = Person('Yash','Kadam',20)
print(Person.classVar)