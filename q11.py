dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
b={}
count=0
for i in dict1.values():
    for j in dict1.values():
        count=count+1
        b["count"]=count
print(b)

