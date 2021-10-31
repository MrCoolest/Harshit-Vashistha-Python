# Make Flexible functions
# Into to *args
# *opreator
# *args

# With *args opreator we can take n num of argument:

# # example :
def all_total(*args):
    ans = 0
    for i in args:
        ans+=i
    return ans

print(all_total(1,2,3,4,5,6,7,8,9,10))


# # a=int(input('Enter any numbers to add:'))
# n=30
# for i in range(n):
#     print('Enter nu, & to end type 0:')
#     a1=int(input())
#     # print('To end the line type End:')
#     if a1 == 0:
#         break
#     else:
#         continue

# print(f'Answer is : {all_total(a1)}')

def all(*args):
    print(args)
    print(type(args))

all(1,2,4,5,6,78,'Ankit')



