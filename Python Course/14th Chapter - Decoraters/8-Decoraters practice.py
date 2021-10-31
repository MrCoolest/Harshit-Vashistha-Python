# from functools import wraps
# def print_function_data(a_function):
#     @wraps(a_function)
#     def inner_function(*args,**kwargs):
#         print('You are calling add function')
#         return a_function(*args,**kwargs)
#     return inner_function    

# @print_function_data
# def add(a,b):
#     '''This numbers take two argument and return their sums'''
#     return a+b
    
# print(add.__doc__, '\n',add(7,3))    

# Secomd way to doooo

from functools import wraps
def print_function_data(a_function):
    @wraps(a_function)
    def inner_function(*args,**kwargs):
        print(f'You are calling {a_function.__name__}')
        print(a_function.__doc__)
        return a_function(*args,**kwargs)
    return inner_function    

@print_function_data
def add(a,b):
    '''This numbers take two argument and return their sums'''
    return a+b
    
print(add(12,5)) 