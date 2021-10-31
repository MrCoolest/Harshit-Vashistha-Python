# Two types loop in list While and for

# l=["Harsh","Parth","Anuraag","Yash"]
# i=0
# while i < len(l):
#     print(l[i])
#     i+=1
 
# #for
 
# for n in l:
#     print(n)

a=input('Enter the names:')
z=input('How many more names you want to add:')
z=int(z)
i=1
b=[a]                                           #practice

while i<=z:
    a=input('Enter more names:')
    b.append(a)
    i+=1 
print(sorted(b))

