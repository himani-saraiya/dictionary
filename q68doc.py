dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
c=[]
b={}
for i in dic:
    for j in dic[i]:
        b[i]=j
c.append(b)
print(c)