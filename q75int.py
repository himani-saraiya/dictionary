x={'a':[1,2,3,4],'b':[5,6,7,8]}
sum=0
dict={}
for i in x:
    for j in x[i]:
        sum=sum+j
    print(sum)
