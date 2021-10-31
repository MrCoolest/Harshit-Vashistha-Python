# exercise = lambda a,,b,c : sum(a)/3

li = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

def easy(a,b):  
    average = []
    for i in zip(a,b):
       average.append(sum(i)/len(i))
    return average   
       

print(easy(li,l2))

lam = lambda a,b : [(sum(i)/len(i)) for i in zip(a,b)]
print(lam(li,l2))


def nolimit(*args):
    av_lis = []
    for pair in zip(*args):
        av_lis.append(sum(pair)/len(pair))
    return av_lis

print(nolimit(li,l2,l3))        

lamb = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(lamb(li,l2,l3))