a={1:100,2:200,3:300}
b={4:400,5:500,6:600}
c={7:700,8:800,9:900}
dict={}
for i in a:
    for j in b:
        for k in c:
            dict.update(a)
            dict.update(b)
            dict.update(c)

print(dict)

