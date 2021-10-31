#palindrome (revrse and not reverse but same)
fil=input('Enter the word:')
# def rev(a):
#     return a [::-1]
# com= rev(fil)    


# def compare(a,b):
#     if a == b:
#         return "yes it's palindrome"
#     else:
#         return "no it's not palindrome"
# print(compare(fil,com)) 

def palindrome(word):
    return word == word[::-1]
print(palindrome(fil))
