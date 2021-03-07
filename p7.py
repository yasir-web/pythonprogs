#WAP to find greatest of three number with nested if else
a=int(input("First number :"))
b=int(input("Second number"))
c=int(input("third number :"))
if a>=b:
	if a>=c:
		print("greatest number is :",a)
	else:
		print("greatest number is :", c)
else:
	if b>=c:
		print("greatest number is :", b)
	else:
		print("greatest number is :", c)
		