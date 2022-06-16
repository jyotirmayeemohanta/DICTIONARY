dict={'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
values=dict.values()
print(values)
num=[45,60,20,30,50]
i=0
while i<len(num):
    a=i
    j=0
    j+=1
    while j<len(num):
        if num[a]>num[j]:
            a=j
        j+=1
    num[i],num[a]=num[a],num[i]
    i+=1
print(num)
# b.sorted(dict.items(),key=lambda x:x[i])
# print(b)