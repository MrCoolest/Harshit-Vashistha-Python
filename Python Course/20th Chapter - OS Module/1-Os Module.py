# import os 

import os 

print(os.getcwd())
# os.chdir(r'E:\HTML')
# os.mkdir('Ankit')

# print(os.path.exists('Ankit'))

# if os.path.exists('Ankit2'):
#     print('Yes exist')
# else:
#     os.mkdir('Ankit2')
#     print('Maked dir')

# open('File.txt','a').close()
# open('File.csv','a').close()
# os.mkdir(r'E:\HTML\Newfoleder')
# print(os.listdir(r'E:\HTML'))
for item in os.listdir():
    print(os.path.join(os.getcwd(),item))

