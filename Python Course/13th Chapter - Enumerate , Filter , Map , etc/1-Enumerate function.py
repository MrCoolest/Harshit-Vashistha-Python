# We use enumerate function with loop to track positionof our items is iterable

# How we can do this without enumerate function
li = ['Ankit', 'Anuraag', 'Dinesh', 'Yogesh', 'Hitesh']
# count = 0
# for items in li:
#     print(f'{count} -----> {items}')
#     count += 1

# With enumerate functions
for i,j in enumerate(li):
    print(f'{i} is {j}')

# Exercise type :::

# Define a function that take two argument 
# 1.) list containing strings 
# 2.) string that want to find in your list
# and this function will return the index of the string in your list and 
# if sting is not present than return -1

# With normal function define
# def find(l,f):
#     if f in l:
#         return l.index(f)
#     return -1    

# print(find(li,'Hitesh'))

# With lambda functiion define
fin = lambda a,b : a.index(b) if b in a else -1
print(fin(li,'Anuraag'))


# With harshit lecture method:

def find_the(x,y):
    for a,b in enumerate(x):
        if b == y:
            return a
    return -1

print(find_the(li, 'Yogesh'))            

