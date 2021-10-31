# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD, COMSTRUCTOR
# WHAT ARE ATTRIBUTE, INSTANCE VARIABLES
# HOW TO CREATE AN OBJECT

class Person :
    def __init__(self,first_name,last_name,age):
        # instance  variables
        self.fname = first_name
        self.lname = last_name
        self.Age = age

p1 = (Person('Ankit','Patwa',19)) #p1 is object or instance variable

print(p1.fname,p1.lname,p1.Age)

