dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a={}
dic=list(dict.values())
dic.sort()
for i in dic:
    for j in dict:
        if i==dict[j]:
            a[j]=i
print(a)
