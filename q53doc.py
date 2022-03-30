dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
c=0
for i in dict.values():
    for j in i:
        c=c+1
print(c)