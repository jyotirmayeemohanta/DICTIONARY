a="MISSISIPPI"
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(str(b))

# {'M':1,'I':4,'S':4,'P':2}

