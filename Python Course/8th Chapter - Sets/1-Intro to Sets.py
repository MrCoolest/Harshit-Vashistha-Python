# Set data type
# unordered collection of unique sets

s={1,2,3}
print(s)

# how to remove duplicate items from list
l=[1,2,3,4,4,4,5,5,7,8,8,8,8,9,2,3,4,6,6,6]
s1= list(set(l))
print(s1)

# To add items in set
s.add(5)
s.add(7)
s.add(4)
print(s)

# To remove items froms sets
s.remove(5)
print(s)
s.discard(8)
print(s)

# Clear method
# s.clear()
# print(s)

# copy method
s2 =s.copy()
print(s2)

# What we items sets can store
s3={1,1.1,2.5,6,'Ankit'} #int,float,string
print(s3)
