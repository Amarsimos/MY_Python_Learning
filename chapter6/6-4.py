dict1 = {'for':'do for', 'while':'do while', 'if':'do if', 'else':'do else','if-else':'do if-else'}
for key,value in dict1.items():#正确的做法应该是将 word 解包为键和值，
    #print(word + ':'+ dict1[word])
    print(key + ':'+ value)
dict1.update({'for-else':'do for-else'})#字典并没有 append 方法

for key,value in dict1.items():
    #print(word + ':'+ dict1[word])
    print(key + ':'+ value)