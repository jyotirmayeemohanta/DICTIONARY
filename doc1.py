d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
# for i in d1.keys():
#     for j in d2.keys():
#         if i==j:
#             d3[i]=d1[i]+d2[j]
# else:
#     d3[i]=d1[i]
#     d3[j]=d2[j]
# print(d3)




for i in d1:
    for j in d2:
        d3=d1[i]+d2[j]
print(d3)







