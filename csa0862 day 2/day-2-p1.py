def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n= int(input("enter the number of staires"))
print("the number of ways to reach the top of a staircase with",n,"steps is",fibonacci(n))


