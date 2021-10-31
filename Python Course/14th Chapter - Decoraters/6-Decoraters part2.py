def Decoraterss(take_function):
    def calling_function(*args,**kwargs):
        print('Hey everyone')
        return take_function(*args,*kwargs)
    return calling_function

@ Decoraterss
def func1(a):
    print(f'Number is {a}')
    
func1(2)

# Example 2 
@ Decoraterss
def sqaues(a):
    return a**2

print(sqaues(8))    