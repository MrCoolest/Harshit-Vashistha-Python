from functools import wraps
def Decoraterss(next_func):
    @wraps(next_func)
    def inner_func(*args,**kwargs):
        '''This inner function '''
        print('Hello everyone')
        return next_func(*args, **kwargs)
    return inner_func

@ Decoraterss
def add(a,b):
    '''this is add function'''
    return a+b

print(add.__doc__)
print(add.__name__)