#factorial of given number with format
n=int(input("Enter the number: "))
fact=1
temp=n
while n>0:
    fact=fact*n
    n=n-1
print(temp, "!=", end=" ")
for i in range(temp,1,-1):
    print(i,"*", end=" ")
print("1", end=" ")
print("=",fact,end=" ")
