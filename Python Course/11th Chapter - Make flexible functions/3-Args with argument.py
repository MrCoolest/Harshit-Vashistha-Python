# Args with argument

def milti(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply*=i
    return multiply

num=[2,3,4,5]
print(milti(*num))     #args with argument unpack the list or tuble    