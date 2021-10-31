# f = open(r"E:\Python coruse\18th Chapter - Read Text Files\Text_file.txt")
# f.read()
# f.close()

# with block
# comtext manager
with open('Text_file.txt') as Ankit_file:
    Ankit_data = Ankit_file.read()
    print(Ankit_data)
print(Ankit_file.closed)
