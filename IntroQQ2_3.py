a=dict()
for i in range(1,16):
 a[i]=i*i
print(a)


print({x:x*x for x in range(1,16) })


dic={}
n=15
i=1
while i<=n:
    c=i*i
    dic[i]=c
    i+=1
print(dic)