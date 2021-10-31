# List comprehension 
# With the help of list comprehension we can creat a list in one line

# Creat a list of Sqares of 1 to 10:
# noraml method 
sq=[]
for i in range(1,11):
    sq.append(i**2)
print(sq)    

# Comprehension method:
Sq2=[i**2 for i in range(1,11)]
print(Sq2)

# Creat a list of negative numbers from 1 to 10:
# noraml method
negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)    

# Comprehension method:
ng=[-i for i in range(1,11)]
print(ng)

# one more example:
# Noraml method
name = ['Ankit','Yash','Parth']
new  = []
for i in name:
    new.append(i[0])
print(name)
print(new)    

# Comprehension method:
new2=[i[1] for i in name]
print(new2)