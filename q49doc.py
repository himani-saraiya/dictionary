a={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print(*(list(a.keys())))
c=(list(a.values()))
for i in range(len(c)):
    print(*(c[i]))
