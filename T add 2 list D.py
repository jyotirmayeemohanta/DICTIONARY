d1=["one","two","three","four","five"]
d2=[1,2,3,4,5]
a={}
for i in d1:
    for j in d2:
        a[i]=j
        d2.remove(j)
        break
print(a)

