# list vs generator
# memory usage, time
# when to use list, when to use generator

import time
t1 = time.time()
l = [i**2 for i in range(100000)]
# print(l)
# t2 = time.time()
# print(t2-t1)
g = (i**2 for i in range(100000))
for i in g:
    print(i)
t2 = time.time()
print(t2-t1)