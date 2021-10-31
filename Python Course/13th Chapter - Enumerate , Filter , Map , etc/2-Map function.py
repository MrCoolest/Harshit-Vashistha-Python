# Map Function
a = [1,2,3,4,5,6,7,8,9]

def Sq(l):
    return l**2

print(map(Sq,a))
# With map function
s=list(map(Sq,a))
print(s)

d=tuple(map(Sq,a))
print(d)    

# With lambda 
x=list(map(lambda z:z**2,a))
print(x)

# with list comprehension 
xy=[i**2 for i in a]
print(xy)

# without lambda , map, or comprehension

new=[]
for i in a:
    new.append(Sq(i))
print(new)    

# Exercise ::

new_exercise =['ab','abc','abcd','abcde','Ankit']

def le(l):
    return len(l)

print(list(map(le,new_exercise)))    

# with lambda 
print(list(map(lambda p: len(p),new_exercise)))

# And with simple way
print(list(map(len,new_exercise)))