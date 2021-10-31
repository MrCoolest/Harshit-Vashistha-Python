# fromkey method

a = {'name' : 'Unknown' , 'age' : 'Unknown'}
print(a)

a1 = dict.fromkeys(('name','age','height'),'unknown')
print(a1)

# get method(useful)
print(a1.get('name'))

if 'name' in a1:
    print('present')
else:
    print('not present')

# With get method 
if a1.get('names'):
    print('present')
else:
    print('Not present')            

# if none ------> False ; else ------> True 

# clear method

a1.clear()
print(a1)    

# copy method

a2=a.copy()
print(a2)
print(a2 is a)

# Defrence between copy method and = mentod

a3 = a
print(a3)
print(a3 is a)