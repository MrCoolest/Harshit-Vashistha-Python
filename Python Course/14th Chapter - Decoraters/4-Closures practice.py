# function returning function is also known as Closures function

def power(p):
    def find_of(n):
        return n**p
    return find_of

square = power(2)
print(square(5))        

cube = power(3)
print(cube(5))


