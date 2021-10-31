def add(a,b):        #def is use for define function
    return a + b

# total = add(10,5) #practice
# print(total)

a = int(input('Enter any number:'))
b= int(input('Enter 2nd number:'))               #int practice
total=add(a,b)
print(f'Here is the total of {a} and {b} :{total}')