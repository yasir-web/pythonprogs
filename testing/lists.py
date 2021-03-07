N = int(input("Enter: "))
i=0
l=[]


while i<N:
    e=input().split()
    if e[0]=="insert":
        l.insert(int(e[1]),int(e[2]))
        i+=1
        
    elif e[0]=="print":
        print(l)
        i+=1
    elif e[0]=="remove":
        l.remove(int(e[1]))
        i+=1
    elif e[0]=="append":
        l.append(int(e[1]))
        i+=1
    elif e[0]=="sort":
        l.sort()
        i+=1
    elif e[0]=="pop":
        l.pop()
        i+=1
    elif e[0]=="reverse":
        l.reverse()
        i+=1
    
   
   
    
        
