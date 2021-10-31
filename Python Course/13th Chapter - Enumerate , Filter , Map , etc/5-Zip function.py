# zip function 

list1 = ['Ankit','Anuraag','Yash','Dinesh']
list2 = ['Patwa','Sigu','Kadam','Padhi']
list3 = [1,2,3,4,5,6]

print(list(zip(list1,list2,list3))) #list

print(dict(zip(list1,list2))) #dictionary

s = (list(zip(list1,list2)))
print(dict(s))