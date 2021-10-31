name=input('Enter your name:')
age=input('Enter your age:')
mov=input('Enter the movies seprated by , :').split(',')
song=input('Enter the songs seprated by , :').split(',')

ent={}
ent['name'] = name
ent['age'] = age
ent['Movies'] = mov
ent['songs'] = song

for i,j in ent.items():
    print(F'{i}:{j}')