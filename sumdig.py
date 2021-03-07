#sum of digits in a number
n=int(input("Enter the number"))
s=0
while n!=0:
    s=s+(n%10)
    n=n//10
print("sum =",s)
