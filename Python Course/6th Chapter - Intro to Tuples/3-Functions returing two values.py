def retu(Value1,value2):
    add = Value1 + value2
    mult = Value1 * value2
    return add , mult

print(retu(4,5))    # it give tuple value

add, mult = retu(4,5)     #its not give tuples valuse because we are taking variables
print(add)
print(mult)             