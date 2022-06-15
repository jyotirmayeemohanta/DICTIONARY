# dict1 = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2'],'jyoti':['Alok']}
# count=0
# for i in dict1:
#     for j in dict1[i]:
#         count=count+1
# print(count)


def Function():
    n=int(input("Enter any no"))
    print("Factors are")
#def Function():
    i=1
    while i<=n:
       if n%i==0:
          print(i)
       i+=1
Function()