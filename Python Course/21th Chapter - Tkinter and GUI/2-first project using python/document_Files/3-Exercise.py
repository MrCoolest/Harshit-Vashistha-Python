# Exercise Question 3: Write a function calculation() such that it can accept two variables and 
# calculate the  addition and subtraction of it. And also it must return both addition and 
# subtraction in a single return call

def calculation(a,b):
    return a+b, a-b

res=calculation(60,40)
print(res)   
print(type(res)) 

add,sub=calculation(100,50)

print(add)
print(sub)