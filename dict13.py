my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
max1=0
max2=0
max3=0
for i in my_dict:
    if my_dict[i]>max1:
        max1=my_dict[i]
    if max2<my_dict[i]<max1:
        max2=my_dict[i]
    if max3<max2>my_dict[i]<max1:
        max3=my_dict[i]
print(max1)
print(max2)
print(max3)
# dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
# max1=0
# max2=0
# max3=0
# for i in dict:
#     if dict[i]>max1:
#         max3==max2
#         max1=dict[i]
#     elif dict[i]>max2:
#         max3==max2
#         max2=dict[i]
#     elif dict[i]>max3:
#         max1==dict[i]
#         max3=dict[i]
# print(max1,max2,max3) 
