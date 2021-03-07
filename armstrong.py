#armstrong number
n=int(input("Enter a number"))
temp=n
temp1=n
sum=0
c=len(str(n))
while n>0:
    r=n%10
    sum=sum+r**c
    n=n//10

if sum==temp:
    print("no. is armstrong")
else:
    print("not armstrong")
