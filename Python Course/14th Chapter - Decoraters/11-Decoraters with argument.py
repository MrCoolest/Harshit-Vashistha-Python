# Decorater with argument
# @ decorater(type)
from functools import wraps
def allow_data_type(data_type):
    def decorater_func(funct):
        @wraps(funct)
        def inner_wrappe_funct(*args,**kwargs):
            if all([(type(i)==data_type) for i in args]):
                return funct(*args,**kwargs)
            return 'Wrong input'
        return inner_wrappe_funct
    return decorater_func

@allow_data_type(list)
def our_function(l):
    s = []
    for i in l:
        s.append(i**2)
    return s    

print(our_function([2,4,5]))
print(our_function([2,4,5],9))