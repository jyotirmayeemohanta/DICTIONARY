# dict1=dict()
# for i in range(1,16):
#     dict1[i]=i**2
# print(dict1)


i=1
c={}
while i<=15:
    c.update({i:i*i})
    i+=1
print(c)

# dict={"brand":"car","model":"sujuki","year":2022}
# print(dict)
# x=dict["model"]
# print(x)
# z=dict.get("year")
# print(z)
# dict={"brand":"car","model":"sujuki","year":2022}
# for i in dict:
#     print(i)

# for i in dict:
#     print(dict[i])
dict={"brand":"car","model":"sujuki","year":2022}
# for i in dict.values():
#     print(i)

# for i in dict.keys():
#     print(i)
# for i in dict:
    # print(i)   brand,model,year

# dict={"brand":"car","model":"sujuki","year":2022}
# for i,j in dict.items():
#     print(i,j)
# dict={"brand":"car","model":"sujuki","year":2022}
# for i in dict:
#     dict["year"]=2020
# print(dict)
dict={"brand":"car","model":"sujuki","year":2022}
dict['model']=2021
print(dict)
# dict={"brand":"car","model":"sujuki","year":2022}
# dict["color"]="bule"
# print(dict)
