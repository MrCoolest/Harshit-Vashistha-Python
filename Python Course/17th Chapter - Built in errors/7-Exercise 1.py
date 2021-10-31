# exercise


def Division(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        print('Do not divide by zero')
    except TypeError:
        print('Do not give string input') 
    


print(Division(4,7))
print(Division(99,0))
print(Division('9',0))