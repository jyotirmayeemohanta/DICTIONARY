




my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in my_dict:
#     print(i,end=" ")
# print("")
# for j in range(len(my_dict)):
#     for k in my_dict:
#         print(my_dict[k][j],end=" ")
#     print()



#  Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
print(*list(my_dict.keys()))
a=(list(my_dict.values()))
for i in range(len(a)):
    print(*(a[i]))
