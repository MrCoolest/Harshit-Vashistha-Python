# 'r' = read
# 'w' = write
# 'a' = append
# 'r+' = read + write

# read mode
# with open('new.txt') as f:
#     print(f.read())

# # write mode
# with open('new1.txt', 'w') as f:
#     f.write('Hello 2')

# # append mode
# with open('new.txt','a') as g:
#     g.write('This is append method')

#r+ mode
# it will overwrite but limited len
with open('new.txt', 'r+') as R_plus:
    R_plus.seek(len(R_plus.read()))
    R_plus.write('\nHelooo aginnnnnnnn\n')  
