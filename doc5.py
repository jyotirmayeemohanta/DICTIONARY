dict={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Values=dict.values()
print(Values)
i=0
while i<len(dict):
    a=i
    j=0
    j+=1
    while j<len(dict):
        if dict[a]>dict[j]:
            a=j
        j+=1
    dict[i],dict[a]=dict[a],dict[i]
    i+=1
print(dict)




# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
