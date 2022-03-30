d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in d1:
    for j in d2:
        if i==j:
            j=j+i
        else:
            dic.update(d1)
            dic.update(d2)
            print(dic)