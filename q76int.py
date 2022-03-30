dic=["puja","rani"]
i=0
dict={}
while i<len(dic):
    j=0
    key=""
    value=""
    count=0
    while j<len(dic[i]):
        if count<=1:
            key+=dic[i][j]
            count+=1
        else:
            value+=dic[i][j]
        j+=1
    dict[key]=value
    i+=1
print(dict)