# dictionaries intro
# Q - Why we use dictionaries?
# A - Because of limitations of list, lists are not enough to reprsent
# real data .

# Example
# user = ['Ankit',19,['Phir hera pheri','3 idiotes'],['Honey sing','King']
# this list contains user name, age , fav movies, fav singers
# you can do this but is not a good way to do this.


# Q - what are dictionaries
# A - unordered collections of data in key : value pair.


# how to create dictionaries
user = {'name' : 'Ankit' , 'age' : 19}
print(user)
print(type(user))

# second method to create dictionaries
user1 = dict(name='ankit' , age = 24)
print(user1)

# how to access data from dictionaries
print(user['name'])  # no indexing...
print(user['age'])  #access data by call the vairable inside dictionary

# which type of data a dictionary can store ?
# anything
# integers , strings , list , tuple , dictionary , etc

user_info = {
    'Name' : 'Shantanu',
    'age' : 23,
    'fav_movie' : [1,2,3,4,5],
    'fav_tunes' : (1,5,7,8,4)
}

print(user_info['fav_tunes'])

p = {
    'q' : {
        's' : 2,
        'h' : 3,
    },
    'r' : {
        't' : 4,
        'u' : 5,
    }
}
print(p)
