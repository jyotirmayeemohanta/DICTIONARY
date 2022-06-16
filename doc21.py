dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
d=[]
for i in dict:
    for j in i.values():
        d.append(j)
print(set(d))                                                                          



