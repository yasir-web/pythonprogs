#Demonstrate the concept of inheritence
class A:
    def showA(self):
        print("The message from class A")
class B(A):
    def showB(self):
        print("The message from class B")
#Now we test the class
b=B()
b.showA()
b.showB()


