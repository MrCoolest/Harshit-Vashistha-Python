name,age=input('Enter your name and age :').split(',')
print('Hello! '+ name +'. your age is '+ str(int(age)+1))
# string Formatting
print('Hello {}. Your age is {}'.format(name,str(int(age)+2))) 
print(f'Hello!{name}, Your age is {str(int(age)+3)}')

