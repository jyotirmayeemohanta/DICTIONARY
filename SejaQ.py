b="sayjal rai "
a={}
c=0
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)

# outpur{"sayjal":6,"space1":1,"rai":3,"space2":2}