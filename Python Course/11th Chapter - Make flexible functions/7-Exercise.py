def naam(l, reverse = False):
    if reverse == True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]    

name =  ['ankit', 'patwa']
print(naam(name, reverse=True))
print(naam(name))
