# Advance sorted function

fruits1=['Mango','Grapes','Orange','Apple']
fruits1.sort()
print(fruits1)

fruits2=('Mango','Grapes','Orange','Apple')
print(sorted(fruits2))

fruits3={'Mango','Grapes','Orange','Apple'}
print(sorted(fruits3))



student2 = [
    {'Name' : 'Ankit', 'Score' : 90, 'age' : 21},
    {'Name' : 'Dinesh', 'Score' : 70, 'age' : 22},
    {'Name' : 'Anuraag', 'Score' : 80, 'age' : 20}
]

An = sorted(student2, key = lambda d : d.get('age'))
print(An)
An = sorted(student2, key = lambda d : d.get('age'), reverse=True)
print(An)
