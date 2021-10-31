# Intro to generators
# Generators 
# generators are iterator

# iterator & iterable

l = [1,2,3,4] #----> iterable

for i in l:
    print(i)

i = iter(l)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

map(lambda a: a**2,l)) #-----> iterator

# list_memory = [............................] , memory store whole list
# generator_memory = () , memory of generator store particular num at one time

