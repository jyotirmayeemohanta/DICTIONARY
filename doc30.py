dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i,j in dict.items():
    for x in " ":
        i=i.replace(x,"")
        d[i]=j
print(d)









# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
