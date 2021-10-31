# List comprehension with if statement :

l=list(range(1,11))
print(l)

# Noraml method:
find_even=[]
for i in l:
    if i%2==0:
        find_even.append(i)
print(find_even)        

# Comprehension method:
even=[i for i in l if i%2==0]
print(even)

# odd numbers with comprehension methods
odd=[i for i in l if i%2!=0]
print(odd)