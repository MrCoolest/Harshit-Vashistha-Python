import os,shutil
# Note: we can any extension in tuple
dict_ext ={
    'document' : ('.py','.html','.c','.cpp','.txt','.css','.htm'),
    'audio' : ('.mp3','.m4a','.wav','.flac'),
    'image' : ('.jpg','.png'),
    'video' : ('.mp4','.mkv','.MKV','.flv','.mpeg')
}
folderpath = input("Enter folder path:")

def file_finder(f_path,f_extension):
    file_name = []
    for files in os.listdir(f_path):
        for extention in f_extension:
            if files.endswith(extention):
                file_name.append(files)
    return file_name            
# print(file_finder(folder_path,image))

for file_ext,filetype in dict_ext.items():
    folder_name = file_ext + '_Files'
    folder_path = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for items in file_finder(folderpath,filetype):
        items_path = os.path.join(folderpath,items)
        items_new_path = os.path.join(folder_path,items)
        shutil.move(items_path,items_new_path)

    # print('Calling new extension files')
    # print(f'{file_finder(folder_path,filetype)}')
