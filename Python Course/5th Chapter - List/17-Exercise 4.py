def odd_even(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i) 
    out=[odd, even]        
    return out
s=[1,2,3,4,5,6,7,8,9]
print(odd_even (s))                   