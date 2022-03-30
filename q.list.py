d=[1,2,3,4,5,6,7,8,9,10]
dict={}
g=[]
e=['c1','c2','c3']
count=0
i=0
while i<len(d):
    for j in e:
        # g.append(d[i])
        if count==3:
            count=count+1
            g.append(d[i])
            dict[j]=g
            # count+=1
    i=i+1
    print(dict)