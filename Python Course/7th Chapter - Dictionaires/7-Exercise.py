# Exercise to print cube in dict
def bd(n):
    a=dict()
    for i in range(1,n+1):
        a[i]=i*i*i
    return a
User=int(input('Enter the num til you want the cube:'))
print(bd(User))

