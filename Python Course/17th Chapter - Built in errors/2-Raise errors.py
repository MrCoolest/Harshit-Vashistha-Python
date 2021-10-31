# raise errors

def int_adds(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('Its not int type , only int type is alowed')    

print(int_adds('2','5'))