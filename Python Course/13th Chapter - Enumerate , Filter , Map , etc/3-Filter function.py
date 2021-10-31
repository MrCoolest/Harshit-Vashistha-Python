# filter function 

num = [1,2,3,4,5,6,7,8,9,10]

def even(l):
    return l%2==0

even_tuple = tuple(filter(even,num))
print(even_tuple)

# With lambda 
print(tuple(filter(lambda a : a%2==0,num)))
