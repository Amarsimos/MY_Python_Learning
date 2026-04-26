filename = 'learning_python.txt'
# print('1st')
# with open(filename) as lp:
#     content = lp.read()
#     print(content)
#     print('----------------')

print('2nd')
with open(filename) as lp:
    # line = lp.readlines()
    for line in lp:
        line_new = line.replace('python','C')#字符串是不可变的,replace方法不会直接修改原字符串，而是返回一个新的字符串
#所以需要将原字符串重新赋值给line_new
        print(line_new.rstrip())
    print('----------------')

# print('3rd')
# lplist = []
# with open(filename) as lp:
#     for line in lp:
#         lplist.append(line.rstrip())
# print(lplist)