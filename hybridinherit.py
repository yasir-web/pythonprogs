#WAP to demonstrate hybrid inheritence
class employee:
    def setemployee(self,empid,empname):
        self.empid=empid
        self.empname=empname
    def getemployee(self):
        print("Employee id: ",self.empid)
        print("Employee name: ",self.empname)
class payroll(employee):
    def setpayroll(self,bs,hra,da):
        self.bs=bs
        self.hra=hra
        self.da=da
    def getpayroll(self):
        print("Base Salary: ",self.bs)
        print("House Rent Allowance: ",self.hra)
        print("Dearness Allowance:",self.da)
class loan:
    def setloan(self,amt):
        self.amt=amt
class payslip(payroll,loan):
    def netsalary(self):
        print("Net salary: ", (self.bs+self.hra+self.da))
        print("Salary on hand: ",(self.bs+self.hra+self.da-self.amt))
#Now we test the classes
ps=payslip()
empid=int(input("Enter Employee Id: "))
empname=input("Enter Employee Name: ")
ps.setemployee(empname,empid)
bs=int(input("Enter Basic Salary: "))
hra=int(input("Enter House Rent Allowance: "))
da=int(input("Enter Dearness Allowances: "))
ps.setpayroll(bs,hra,da)
amt=int(input("Enter Monthly EMI: "))
ps.setloan(amt)
print("**************** PAY SLIP***************")
ps.getemployee()
ps.getpayroll()
ps.netsalary()