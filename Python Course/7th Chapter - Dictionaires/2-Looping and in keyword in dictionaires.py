# in keyword and iteration in dictionaires

user_info={
    'Name' : 'Ankit',
    'Age' : 19,
    'Fav_movies' : ['Abc','xyz'],
    'fav_song' : ['123','456'],
}

# Check if key exist in dictionary
if 'Name' in user_info:
    print("present")
else:
    print("Not Present")

# Check if value exist in dictionary --------> Values method
if 'Ankit' in user_info.values():
    print('Yes it is in')
else:
    print('No it is not in')  


# Loops in dictionary
for i in user_info:    # ---> It will print only keys of dictionary
    print(i)

# For printing values in dictionary  
for i in user_info.values():
    print(i)

# Values method
user_info_values = user_info.values()
print(user_info_values)

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)

# Second way to print values in dictionaries
for i in user_info:
    print(user_info[i])       

# items method
user_info_items = user_info.items()
print(user_info_items)


for key,Value in user_info.items():
    print(f'key is {key} and values is {Value}')