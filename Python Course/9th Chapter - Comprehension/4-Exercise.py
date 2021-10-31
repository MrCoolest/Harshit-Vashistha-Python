# l=['Ankit', True, False, (1,2,3,4),1,1.5,5,76]
# lis=[str(i) for i in l if type(i)==int or type(i) == float]
# print(lis)

def ch(l):
    return [str(i) for i in l if type(i) == int or type(i) == float]


b = ['Ankit', True, False, (1,2,3,4),1,1.5,5,76]
print(ch(b))
