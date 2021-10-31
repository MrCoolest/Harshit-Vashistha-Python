num=list(range(1,11))
print(num)
num2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sq(l):
    squ=[]
    for i in l:
        i*i
        squ.append(i*i)
    return squ
print(sq(num))        
        
