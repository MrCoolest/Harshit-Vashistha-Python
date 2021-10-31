def comm(a,b):
    c=[]  
    for i in a:
        if i in b:
            c.append(i)
    return c 

x=[1,2,3,4,5,6,7,8]
y=[1,4,5,6,8] 
print(comm(x,y))   
         