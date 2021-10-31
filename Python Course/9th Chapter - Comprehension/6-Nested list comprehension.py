li=[[1,2,3],[1,2,3],[1,2,3]]
print(li)

# Normal method
lis=[]
for i in range(3):
    lis.append([1,2,3])
print(lis)  

# Comprehension method;

lis2=[[i for i in range(1,4)] for i in range(3)]
print(lis2)
