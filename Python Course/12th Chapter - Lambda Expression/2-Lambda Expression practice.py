# Lambda expresion practice

# normal function
def Check(a):
    if a%2==0:
        return True
    return False    
print(Check(9))  

# With lambda function
Even = lambda a : a%2==0 
print(Even(4))

# reverse String
# noraml way
def rev(a):
    return a[::-1]
print(rev('Ankit Patwa'))

# With Lambda 
rev2 = lambda a: a[::-1]
print(rev2('aNKIT pATWA'))

# with if else
# normal way
def lenth(a):
    if len(a) > 5:
        return True
    return False
print(lenth('Ankit')) 

lenth2 = lambda a : True if len(a) > 3 else False
print(lenth2('Ankit'))