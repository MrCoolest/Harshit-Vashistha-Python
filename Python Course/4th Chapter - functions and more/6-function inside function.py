# Function inside function
x=int(input('Enter the first value:'))
y=int(input('Enter thr second value:'))
z=int(input('Enter the third value:'))
def great(a,b):
    if a>b:
        return a
    return b    
def greatest(a,b,c):
    big=great(a,b)
    return great(big,c)
print(greatest(x,y,z))    