# #here we want to print fibonacci series 
# # >> 0 1 1 2 3 5 8 13 21 34.........

# a=int(input('Enter til you want to print Fibonacci numbers:'))


# def fibonacci (num):
#     first=0
#     second=1
#     if num==1:
#         print(first)
#     elif num==2:
#         print(first, second)
#     else:
#         print(first,second,end=" ")
#         for i in range (num-2):    
#             third=first+second                    #it is use for changing the values 
#             first=second
#             second=third
#             print(second,end=" ")
# fibonacci(a)
                

###############taking two input from start to end:

a=int(input('Enter the starting number:'))
b=int(input('Enter second num to add:'))
c=int(input('Enter how many num you want from starting:'))

def fibo (n):
    a2=a
    b2=b
    for i in range (n-2):   #not perfect its practice 
        c2=a2+b2
        a2=b2
        b2=c2
        print(a2,b2,end=" ")
fibo(c)            
    