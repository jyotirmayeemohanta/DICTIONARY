dict1={"a":54,"b":76,"c":99,"u":89}
sum=0
for i in dict1.values():
    sum=sum+i
print(sum)

dict1={"a":54,"b":76,"c":99,"u":89}
sum=0
for i in dict1:
    sum=sum+dict1[i]
print(sum)
