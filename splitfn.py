#WAP to take user full name as input and display Short name
name=input("Enter Full Name: ")
shortname=name.split()
#print(shortname)
print("Your short name is =",end="")
for i in range(len(shortname)-1):
    print(shortname[i][0]+".",end="")
print(shortname[len(shortname)-1])

