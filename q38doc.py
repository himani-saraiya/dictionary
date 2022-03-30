dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in dic1:
    for j in dic2:
        if i==j:
            dic[j]=dic1[i]+dic2[j]
else:
    dic[i]=dic1[i]
    dic[j]=dic2[j]        
print(dic)