# Counting words

def counter(a):
    count={}
    for i in a:
        count[i]=a.count(i)
    return count
b=input('Enter the name:')
print(counter(b))
 