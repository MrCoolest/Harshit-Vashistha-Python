
# # total=0
# # i=1
# # while i<=10:
# #     total= total+i
# #     i = i+1
    
# # print(total)
# a=int(input('Enter any number 1 to till you want sum:'))
# total=0
# i=1
# while i<=a:
#     total+=i
#     i+=1
# print(f'sum of 1 to {a} is:{total}')    

table=int(input('Enter the  table you want:'))
til=int(input('Enter the table till you want:'))
i=1
b=0
while i<=til:
    b=table*i
    print(f'{table} X {i} = {b}')
    i+=1