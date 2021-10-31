import pdb # import db module

# module - python file contains useful classes and functions wrote by developer.

# According to wikipedia - Debugging is the process of finding and resolving defects
# of problems with in a computer program that prevent correct operation of computer
# software or a system

# why debugging
# 1) our program is not running and causing unexpected errors
# 2) our programs is woring fine bu not working the same way we want

# steps for debugging
#  1) set trace
#  2) execute code line by line
pdb.set_trace()
name = input('Enter your name : ')
age = input('Enter your age : ')

age2 = int(age) + 5

print(f'{name} your age is {age2}')

# pdb commands

# l - list
# q - quite
# c - continue
# n - execute next line