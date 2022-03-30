a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
dict={}
for i in a:
    j=0
    n=[]
    while j<len(a[i]):
        if a[i][j]%2==0:
            n.append(a[i][j])
            dict[i]=n
        j+=1
print(dict)