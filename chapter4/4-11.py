friuts = ['apple', 'banana', 'orange', 'grape', 'pear']
# print('The first three fruits are: \n', friuts[:3])
# print('The middle three fruits are: \n', friuts[1:4])
# print('The last three fruits are: \n', friuts[-3:])
friends_friuts = friuts[:]
friuts.append('watermelon')
friends_friuts.append('kiwi')
print('my favorite fruits are:')
for friut in friuts:
    print(friut)
print('my friend favorite fruits are:')
for friut in friends_friuts:
    print(friut)