dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a={}
dic=list(dict.values())
dic.sort()
for i in dic:
    for j in dict:
        if i==dict[j]:
            a[j]=i
print(a)