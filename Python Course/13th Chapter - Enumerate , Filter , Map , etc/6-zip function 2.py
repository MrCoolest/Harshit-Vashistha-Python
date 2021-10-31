# more about zip function

li =[1,3,5,7,9]
l2 =[2,4,6,8,10]
new_list = [max(i) for i in zip(li,l2)]
print(new_list)

l = [(1,2),(3,4),(5,6),(7,8),(9,10)]
# * operater with zip
print(list(zip(*l))) 

li , lis = zip(*l)
print(li) 
print(lis)

new2 = []
for i in zip(li,l2):
    new2.append(max(i))
print(new2)    