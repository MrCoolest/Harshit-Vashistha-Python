# Exercise Question 6: Write a recursive function to calculate the sum of numbers from 0 to 10

def recursive(a):
    ans=0
    for i in range(0,a+1):
        ans+=i
    print(ans) 

recursive(10)       