Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in Boys.keys():
    if key in Dict.keys():
        print (True)
    else:       
        print (False)