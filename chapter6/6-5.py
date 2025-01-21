dict1 = {'neil':'egypt','Amazon':'Amarica','changjiang':'china'}
for key,values in dict1.items():
    print('The ' + key.title() + ' runs through ' + values.title())


for revier in dict1.keys():
    print(revier.title())
for country in dict1.values():
    print(country.title())