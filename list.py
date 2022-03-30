a=[[1,2,3],[1,2,1],[5,3,5],[0,0,3]]
i=0
max=0
list=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        # list.append(sum)
        j=j+1
    list.append(sum)
    i=i+1
print(list)
for k in list:
    if k>max:
        max=k
print(max)
