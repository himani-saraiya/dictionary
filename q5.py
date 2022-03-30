list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
dic={}
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        dic[list1[i]]=list2[j]
        j=j+1
    i=i+1
print(dic)

