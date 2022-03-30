d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'f': 300, 'g': 200, 'd':400}
d={}
for i in d1:
    for j in d2:
        j=j+i
        d.update(d1)
        d.update(d2)
print(d)