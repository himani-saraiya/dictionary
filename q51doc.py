dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max1=0
max2=0
max3=0
for i in dict:
    if dict[i]>max1:
        max3==max2
        max2=max1
        max1=dict[i]
    elif dict[i]>max2:
        max3=max2
        max2=dict[i]
    elif dict[i]>max3:
        max3=dict[i]
print(max1,max2,max3)
        
        