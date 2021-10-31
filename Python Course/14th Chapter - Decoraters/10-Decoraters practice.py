
def only_int(func):
    def inner(*args):
        data_type = []
        # for i in args:
        #     data_type.append(type(i) == int)
        # if all(data_type):  
        #     return func(*args)
        # else :
        #     return 'Wrong input'     
        if all([(type(i) == int) for  i in args]):
            return func(*args)
        return 'Wrong input'    
    return inner        
@only_int
def totl(*args):
    total = 0
    for i in args:
        total+=i
    return total

print(totl(1,2,3,9))