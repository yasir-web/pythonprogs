# list of prime numbers
for a in range(1,101):
	count=0
	i=1
	while i<=a:
		if a%i==0:
			count=count+1
		i=i+1
	if count==2:
		print(a, end=" ")
	
	