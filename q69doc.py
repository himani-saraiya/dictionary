dict={"a":51,"b":22,"c":333,"d":44}
list=[]
maxi=0
sec=0
third=0
for i in dict:
    if dict[i]>maxi:
        maxi=dict[i]
        for j in dict:
            if dict[j]<maxi and dict[j]>sec:
                sec=dict[j]
                for k in dict:
                    if dict[k]<sec and third<dict[k]:
                        third=dict[k]
print(maxi)
print(maxi)
print(sec)
print(third)
s=third,sec,maxi
list.append(s)
print(list)
