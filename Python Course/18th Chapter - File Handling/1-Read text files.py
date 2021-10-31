# read files
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

f = open(r"E:\Python coruse\18th Chapter - Read Text Files\Text_file.txt")
# print(f'curser start from Here :{f.tell()}')
# print(f.read())
# print(f'curser end Here :{f.tell()}')
# print('Before seek method')
# f.seek(0)
# print('After seek method')
# print(f.read())
# print(f'curser end Here :{f.tell()}')
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readlines())

print(f.name)

print(f.closed)

f.close()

print(f.closed)
