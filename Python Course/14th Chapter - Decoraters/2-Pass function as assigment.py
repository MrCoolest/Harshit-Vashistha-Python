# Pass function as assigmen

list1 = [1,2,3,4,5,6,7,8,9]
def squares(a):
    return a**2

# map

print(list(map(squares, list1)))

# Self my map, which is taking function as argument
def My_map(func,a):
    my = []
    for i in a:
        my.append(func(i))
    return my

print(My_map(squares,list1))        

# With lambda
print(My_map(lambda a: a**2,list1))


# 2nd my_map with lsit comprehension :

def my_map2(func,l):
    return [func(i) for i in l]

print(my_map2(squares,list1))   

# With lambda 

Lame = lambda fun, a : [fun(i) for i in a]
print(Lame(lambda s : s**2,list1))