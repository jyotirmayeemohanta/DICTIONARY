d1=[1,2,3,4,5]
d2=["one","two","three","four","five"]
d3={}
for i in range(len(d1)):
    d3[d1[i]]=d2[i]
print(d3)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = dict.fromkeys(keys)
for i, k in enumerate(d.keys()):
	d[k] = values[i]
print(d)