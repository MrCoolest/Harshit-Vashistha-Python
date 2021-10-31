# update dectionary
user_info ={
    'name' : 'Ankit',
    'age' : 19,
    'fav food' : ['123','456'],
    'fav thing' : ['abc','def'],
}
more_info ={'Home town' : 'Delhi', 'Hobbies'  : ['Making memes','eating food']}

user_info.update(more_info)
print(user_info)

ak={'name' : 'Ankit Patwa'}
user_info.update(ak)
print(user_info)