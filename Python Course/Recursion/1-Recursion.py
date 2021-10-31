# # Recusrion 1st
# def print_element(a):
#     if len(a) == 0:
#         return
#     else:
#         print(a[0])
#         print_element(a[1:])     

# print_element([1,2,3,4,5,6,7])        

# --------------------------------------------------------------------------------------------------------------------------------
def print_element2(a, start, end):
    if start >= end+1:
        return 
    else:
        print(a[start])
        print_element2(a, start+1, end)

l = [1,2,3,4,5,6,7,8]
s = 0
e = len(l) - 1

print_element2(l,s,e)
            