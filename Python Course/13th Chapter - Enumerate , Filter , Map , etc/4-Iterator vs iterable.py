# iterator vs iterable

num = [1,2,3,4,5] #iterable ----> tuples,list,string
test = map(lambda a : a**2, num) #iterator
print(test) 

for i in num:
    print(i)

nums = iter(num)  #iterable #this is how for loop works
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

print(next(test)) #iterator is doing direct no nead to use iter function
print(next(test))



