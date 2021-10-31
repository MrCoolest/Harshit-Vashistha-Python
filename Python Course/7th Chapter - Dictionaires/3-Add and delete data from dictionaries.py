# Add and Delete data from dictionaries

user_info={
    'Name' : 'Ankit',
    'Age' : 19,
    'fav food' : ['Every things'],
    'fav thing' : ['Sleep'],
}

# Add method 
user_info['class']=('Bsc-It')
print(user_info)

# pop method 
pops= user_info.pop('fav thing')
print(user_info)
print(pops)
print(type(pops))

# popitems method
pops_item = user_info.popitem()
print(user_info)
print(f'This is popped item {pops_item}')
print(type(pops_item))