# Generator only print even numbers from 1 to input

def even_nums(a):
    for i in range(1,a+1):
        if i%2==0:
            yield i
            
for i in even_nums(20):
    print(i)            


