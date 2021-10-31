import os
import shutil
a = os.walk('E:\\Html')

# for path,folders,Files in a:
#     print(f'Current_path = {path}')
#     print(f'folder_names = {folders}')
#     print(f'Files names = {Files}')

# print(os.getcwd())
# os.mkdir('Ankit/new')
# shutil.rmtree('Ankit')
# shutil.copytree('Ankit1','Ankit2/Ankit1')
shutil.copy('File.csv','Ankit1/File.csv')
# shutil.move('Ankit2','Ankit1/Ankit2')
# shutil.move('File.txt','Ankit1/Ankit2/File.txt')