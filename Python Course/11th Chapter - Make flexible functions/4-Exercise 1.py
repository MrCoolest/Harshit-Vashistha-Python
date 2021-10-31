def power(a,*args):
    if args:
        return [i**a for i in args] 
    else:
        return 'Its empty'

nums=[2,3,4]
print(power(2,*nums))
print(power(3,*nums))
