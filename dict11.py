dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
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
        max1=dict[i]
print(max1,max2,max3)