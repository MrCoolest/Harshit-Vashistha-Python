class Person:
    def __init__(self,first,last,age):
        # instance variable / object name
        self.first = first
        self.last = last
        self.age = age

        # Instance method
    def ful_name(self):
        return f"{self.first} {self.last}"

    def check(self):
        return self.age > 18    


p1 = Person('Ankit','Patwa',19)

print(p1.first)
print(p1.ful_name())
print(Person.ful_name(p1))

print(p1.check())
print(Person.check(p1))
