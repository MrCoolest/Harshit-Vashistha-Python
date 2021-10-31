# args with parameter

def MUltipliy(num,*args):
    multi = 1
    print(num)
    print(args)
    for i in args:
        multi*=i
    return multi    

print(MUltipliy(2,2,5,1))

