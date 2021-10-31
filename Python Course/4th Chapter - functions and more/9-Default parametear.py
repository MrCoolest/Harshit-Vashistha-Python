# Default parameters
a=input('Enter your name:')
b=input('Enter your last name:')
c=input('Enter your age:')
c=int(c)
def detail(name,last,age): #the last parameter is only define default
    print(f'Name is {name}')
    print(f'last name is {last}')
    print(f'age is {age}')
    
detail(a,b,c)
