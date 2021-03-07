    #function- function is a  named block of code which performs a specific task, by using function you can avoid to write same code over and over
    #syntax to create a function: def function_name(parameters):
        #code
#eg- def add(x,y):
    #return(x+y)
def add(x,y):
    return(x+y)
a=int(input("first number: "))
b=int(input("second number: "))
s=add(a,b)
print(s)
