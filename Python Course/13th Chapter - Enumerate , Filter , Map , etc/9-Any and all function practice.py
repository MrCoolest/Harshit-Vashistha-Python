# any() , all() function practice

def check(*args):
    if all([(type(value) == int or type(value) == float) for value in args]):
        total = 0
        for i in args:
            total+=i
        return total
    else:
        return 'Wromg input'

print(check(1,2,3,4,5,9.0))     

print(check(1,2,3,4,5,9.0,'Ankit'))       