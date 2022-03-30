dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
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
print(maxi,sec,third)
        