#wap to find the factorial of given number using recurssion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
x=int(input("Enter the number: "))
f=fact(x)
print(f)
