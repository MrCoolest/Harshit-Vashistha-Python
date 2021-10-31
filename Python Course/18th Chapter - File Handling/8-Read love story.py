# read emojis notes
# with open('love story.txt','r', encoding='Utf-8') as f:
#     print(f.encoding)
#     print(f.read())
    

# long file
with open('pys.txt','r') as long_file:
    data = long_file.read(100)
    while len(data)>0:
        print(data)
        data = long_file.read(100)