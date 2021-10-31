a=list(range(1,11))
print(a[::-1])
def ret(l):
    return l[::-1]
print(ret(a))      

def rev(lis):
    sq=[]
    for i in range(len(lis)):
        poped=lis.pop()
        sq.append(poped)
    return sq    
print(rev(a))        