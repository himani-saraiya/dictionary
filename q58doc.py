dic={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
dict={}
for i,j in dic.items():
    j.clear()
    dict[i]=j
print(dict)
    