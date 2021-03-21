# WAP to search for a substring inside a string
s1 = 'abcdcdc'
s2 = 'cdc'
c=0
for i in range(0, len(s1)):
    #for j in range(0, len(s2)):
    t1=s1[i:i+len(s2)]
    # t2 = s2[0:2]
    if t1 == s2:
        c += 1
print(c)

