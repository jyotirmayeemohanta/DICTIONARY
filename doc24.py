dict=[{'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}]
d={}
for i in dict:
    if i['item'] in d.keys():
        d[i['item']]+=i["amount"]
    else:
        d[i['item']]=i["amount"]
print(d)











# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})
