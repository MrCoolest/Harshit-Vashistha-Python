# kwargs (key arguments)
# **Kwargs (Double star operaters)

# kwargs as a parameter 
def sample(**kwargs):
    print(kwargs)
    print(type(kwargs))


sample(name = 'Ankit', age = 19, hobbies ='making memes')

def sample2(**kwargs):
    for i,j in kwargs.items():
        print(f'{i} is {j} ')


sample2(name = 'Ankit', age = 19, hobbies ='making memes')  
a = {'name':'ANKIT PATWA', 'Interest':'Listing songs'} 

sample2(**a) #**argument unpack the dictionary
