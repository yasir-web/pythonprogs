n=int(input("Enter a number"))
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse no. :", rev)
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")
