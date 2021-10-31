# any() , all() fumction

num1 = [2,4,6,8,9]
num2 = [1,2,3,4,5,6,7,8]
check_num = []
for i in num1:
    check_num.append(i%2==0)
print(check_num)    

print(all([True, True, True, True, True])) #------> True
print(all([True, True, False, True, True])) #------> False

# all() saare true hone chaiye
print(all([i%2==0 for i in num1]))

# any() koi bhi ek true hona chaiye
print(any([i%2==0 for i in num1]))