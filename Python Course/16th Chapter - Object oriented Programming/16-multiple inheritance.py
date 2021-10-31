# Multiple inheritance

class A:

    def from_class_a(self):
        return 'Method from class A'

    def hello(self):
        return 'Hello from Class A'    

class B:

    def from_class_b(self):
        return 'Method from class B'

    def hello(self):
        return 'Hello from Class B'

class C(A,B):
    pass

inheritance_c = C()

print(inheritance_c.from_class_a())
print(inheritance_c.from_class_b())
print(inheritance_c.hello())

# method resolution order
# print(help(C))
print(C.mro())
print(C.__mro__)

