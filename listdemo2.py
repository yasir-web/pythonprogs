#make a list and input names of five people in list from user and then sort it in asscending order
list1=[]
print("Enter five names in list")
i=0
while i<5:
    name=input()
    list1.insert(i,name)
    i=i+1
list1.sort()
print("list of elemets in soreted order")
for name in list1:
    print(name)