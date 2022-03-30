d=[1,2,3,4,5,6,7,8,9,10]
dict={}
e=['c1','c2','c3']
g=[]
count=1
i=0
j=0
while i<len(d):
    for j in e:
        if count==3:
            g.append(d[i])
            dict[j]=g
        count+=i
    i=i+1
print(dict)