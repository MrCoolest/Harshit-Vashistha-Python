from functools import wraps
import time
def Calulate_time(a):
    @ wraps(a)
    def inner_one(*args,**kwargs):
        t1 = time.time()
        returns = a(*args,**kwargs)
        t2 = time.time()
        tim = t2 - t1
        print(f'This function tooks {tim} too run')
        return returns
    return inner_one    


@Calulate_time
def func1(a,b):
    print('This is function')
    adds = a + b
    multi = a*b
    print(adds)
    print(multi)
    return adds - multi

# print(func1(6,9))    

@Calulate_time
def Sq(s):
    return [i**2 for i in range(1,s+1)]

print(Sq(100))
