#to find number of digits in a number
n=int(input("Enter the number to be checked: "))
count=0
while n>0:
  count=count+1
  n=n//10
print("number of digits =", count)
