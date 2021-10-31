# Advance min() max() function

# basic :
n = [1,2,3,4,5,6,7,8]
print(max(n))
print(min(n))

# How to check max & min lenth of strings :
strings = ['Ankit','Anuraag','Parth','Dinesh','ab','ba']
print(max(strings, key=lambda a : len(a))) #-----> MAX
print(min(strings, key=lambda a : len(a))) #-----> MIN

student1 = {
    'Ankit' : {'Score' : 90, 'age' : 21},
    'Dinesh' : {'Score' : 70, 'age' : 22},
    'Anuraag' : {'Score' : 80, 'age' : 20}
} 
print(max(student1, key=lambda a : student1[a]['age']))

# student2 = [
#     {'Name' : 'Ankit', 'Score' : 90, 'age' : 21},
#     {'Name' : 'Dinesh', 'Score' : 70, 'age' : 22},
#     {'Name' : 'Anuraag', 'Score' : 80, 'age' : 20}
# ]

# print(max(student2, key=lambda a : a.get('Score'))['Name'])