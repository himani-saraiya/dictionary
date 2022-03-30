a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
i=0
b=[]
for i in a:
    for j in i.values():
        b.append(j)
print(set(b))