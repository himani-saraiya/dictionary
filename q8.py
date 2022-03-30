l=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
b=[]
while i<len(l):
    k=l[i]
    for j in k.values():
        if j not in b:
            b.append(j)
        i=i+1
print(b)

    