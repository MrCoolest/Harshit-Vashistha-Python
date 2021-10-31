#Exercise 3
def revers(x):
    rev=[]
    for i in x:
        rev.append(i[::-1])
    return rev     
    

a=['Ankit','Yash','Deepak']
print(revers(a))