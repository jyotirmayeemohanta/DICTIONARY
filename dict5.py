list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
a={}
while i<len(list1):
    a[list1[i]]=list2[i]
    i+=1
print(a)


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
a={}
while i<len(list1):
    b=list1[i]
    c=list2[i]
    a[b]=c
    i+=1
print(a)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = dict.fromkeys(keys)
for i, k in enumerate(d.keys()):
	d[k] = values[i]
print(d)
