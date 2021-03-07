#WAP to perform write operation
empid=int(input("Enter Employee id: "))
empname=input("Enter Employee name: ")
salary=int(input("Enter Employee Salary: "))
f=open("emp.txt","a")
f.write("Employee ID="+str(empid)+"\n"+"Employee name="+empname+"\n"+"Employee Salary="+str(salary)+"\n")
f.close()
print("Information is Saved in the file ")