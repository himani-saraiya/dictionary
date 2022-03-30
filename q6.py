dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dict={}
for i,j in dic.items():
    if dic[i] not in dict.values():
        dict[i]=j
print(dict)
    