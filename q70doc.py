# dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# l=[]
# dict={}
# for i in dic:
#     for j in dic.values():
#         if i==j:
#             i=i+j
#             dict[i]=j
# print(dict)

data = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

def func(d):
    result = list(map(dict, zip(*[[(key, value) for value in values] for key, values in d.items()])))
    return result
result = func(data)
print(result)