t=int(input("Enter The Temprature: "))
a=int(input("Ennter 1 to covert to fahrenheit or Enter 2 to covert to celcius: "))
temp=t
if a==1:
    t=(temp*1.8)+(32)
    print("Temprature in Fahrenheit is: ",t,"\N{DEGREE SIGN}","F")
elif a==2:
    t=(temp-32)*(5/9)
    print("Temprate is celsuis is: ",t,"\N{DEGREE SIGN}","C")
else:
    print("Invalid input")