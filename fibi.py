# 0 1 1 2 3 5 8
t=int(input("Enter how many terms: "))
n1=0
n2=1
if t==1:
	print(0)
elif t>=2:	
	print(n1,n2,end=" ")
while t-2>0:
	n3=n1+n2
	print (n3, end=" ")
	n1=n2
	n2=n3
	t=t-1
