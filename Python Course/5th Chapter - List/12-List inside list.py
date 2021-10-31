#list inside list

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat)

for sublist in mat:
    for subnum in sublist:
        print(subnum)



print(mat[1][1])        