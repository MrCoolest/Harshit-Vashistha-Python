# Dictionary comprehension
square = {1:1, 2:4, 3:9, 4:16, 5:25}

# normal method
# s=dict()
# for i in range(1,11):
#     s[i]=i**2
# print(s)    

# comprehension method:
sq = {i:i**2 for i in range(1,11)}
print(sq)
sh = {f'Square of {i} is' :j for  i, j in sq.items()} 
print(sh)
sq1 = {f'cube of {i}: is' : i**3 for i in range(1,11)}
print('\n \n \n', sq1)
for h,w in sh.items():

    print(f'{h} : {w}')


# Word count in dictionary in comprehension method:
name = "Ankit Bhagwan Patwa"
count={char:name.count(char) for char in name}
print(count)
for x,y in count.items():
    print(f'{x} : {y}')