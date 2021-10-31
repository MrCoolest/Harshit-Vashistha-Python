# Exercise Question 8: Generate two Python list of all the even and odd numbers between 1 to 30.

def even_odd(a,b):
    even=[]
    odd=[]
    for i in range(a,b+1):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f'Odd list is {odd}')
    print(f'Even list is {even}') 

x=int(input('Enter the number from start:')) 
y=int(input('Enter the number till end:'))     

even_odd(x,y)                         