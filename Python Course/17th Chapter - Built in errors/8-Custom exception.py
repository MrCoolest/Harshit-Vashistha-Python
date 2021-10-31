# Python Custom exception
# Q - Why we use custom errors
# A - To increase the readability of code.

class Lenthisshort(ValueError):
    pass

def Validation(name):
    if len(name) < 5:
        raise Lenthisshort('Its less than 5')
    return name


username = input('Enter the name:')
print(f'hello {Validation(username)}')
