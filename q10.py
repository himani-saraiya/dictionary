l="MISSISSIPPI"
m={}
for i in l:
    if i in m:
        m[i]=m[i]+1
    else:
        m[i]=1
print(str(m))
