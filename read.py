#program to perfrom read operation in a file
f=None
try:
    filename=input("Enter the file name to be opened: ")
    f=open(filename,"r")
    content=f.read()
    print(content)
except FileNotFoundError:
    print("File does not Exist")
finally:
    if f!=None:
        f.close()