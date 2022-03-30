data = {'id1':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},'id2':{'name': ['David'],'class': ['V'], 'subject_integration': ['english, math, science']},'id3':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},'id4':{'name': ['Surya'],'class': ['V'],'subject_integration': ['english, math, science']}}
a={}
b=set(data)
for i in b:
    for j in b:
        if b[i] not in a:
            if b[j] not in a:
                a.update(b[i])
                a.update(b[j])
print(a)

 

