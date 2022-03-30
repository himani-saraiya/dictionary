dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
a={}
for i,j in dic.items():
    for k in i:
        if k in " ":
            i=i.replace(k,"")
            a[i]=j
print(a)
    