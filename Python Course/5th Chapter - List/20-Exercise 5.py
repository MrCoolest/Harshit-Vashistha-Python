def ty(l):
    tot=0
    for i in l:
        if type(i) == list:
            tot+=1 
    return tot
    
a=[5,54,52,5,2,[455,52,52]]
print(ty(a))        