from collections import OrderedDict

dict1 = OrderedDict()
dict1['for'] = 'do for'
dict1['if'] = 'do if'
dict1['while'] = 'do while'
dict1['else'] = 'do else'
dict1['if-else'] = 'do if-else'


for key,value in dict1.items():#正确的做法应该是将 word 解包为键和值，
    #print(word + ':'+ dict1[word])
    print(key + ':'+ value)
dict1.update({'for-else':'do for-else'})#字典并没有 append 方法

for key,value in dict1.items():
    #print(word + ':'+ dict1[word])
    print(key + ':'+ value)