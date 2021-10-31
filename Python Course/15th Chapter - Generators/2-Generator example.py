# Creating first generator with generator function
# 1.) generator function
# 2.) generator comrehension

# IN THIS WE WILL LEARN ABOUT GENERATOR FUNCTION

def num(a):
    for i in range(1,a+1):
        yield i

print(num(5))        

for i in num(5):
    print(i)     #Generator is iterator so it only print one time after printing, it will get delete from memory

