# raise error example 1
# NotImplementedError
# abstract

class Animal:
    def __init__(self, name):
        self.name = name

    #abstract error 
    def sound(self):
        raise NotImplementedError('Def your main class sound')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'Bhoww Bhoww'    

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed                   

    def sound(self):
        return 'mewo mewoo'

dog1 = Dog('Dj', 'xyz')
print(dog1.sound())        

Cat1 = Cat('Katy','Abc')
print(Cat1.sound())