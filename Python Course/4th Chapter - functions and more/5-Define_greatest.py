# a=int(input('Enter the first:'))
# b=int(input('Enter the Second:'))
# c=int(input('Enter the third:'))

# def gretest(x,y,z):
#     if x>y:
#         if x>z :
#             return f"{a}"
#     else:
#         if y>z:
#             return f"{b}"
#     return f"{c}"            
# print(gretest(a,b,c))    

#########   WITH OPERATORS

a=int(input('Enter the first:'))
b=int(input('Enter the Second:'))
c=int(input('Enter the third:'))

def gretest(x,y,z):
    if x>y and x>z:
        return f"{a}"
    else:
        if y>z:
            return f"{b}"
    return f"{c}"            
print(gretest(a,b,c))    