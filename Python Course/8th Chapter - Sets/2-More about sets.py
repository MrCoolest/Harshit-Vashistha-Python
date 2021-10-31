# in keyword in sets or for loop

s={'a','n','k','i','t',1,9}

# in keyword to check if item is present or not in set

if 'n' in s:
    print('present')
else:
    print('not present')    

# for loop
for item in s:
    print(item)

s1 = {1,2,3,4,5}
s2 = {4,3,5,8,9}

print(s1 | s2) #union collection of set

print(s1&s2) #intersection collection of sets
