#genrate list with range function
#Something more about pop
#index method
#pass list a function

#range function
num=list(range(1,11))
print(num)

#pop
print(num.pop())

#index method
print(num.index(2))

num2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def neg(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(neg(num2))               