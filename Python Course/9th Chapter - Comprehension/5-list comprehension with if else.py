num = list(range(1,11))
# Noraml method
new=[]
for i in num:
    if i%2==0:
        new.append(i*2)
    else:
        new.append(-i)   
print(new)        

# Comprehension method:
new2=[i*2 if i%2==0 else -i for i in num]
print(new2)