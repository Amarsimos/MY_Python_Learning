filename = 'learning_python.txt'
print('1st')
with open(filename) as lp:
    content = lp.read()
    print(content)
    print('----------------')

print('2nd')
with open(filename) as lp:
    # line = lp.readlines()
    for line in lp:
        print(line.rstrip())
    print('----------------')

print('3rd')
lplist = []
with open(filename) as lp:
    for line in lp:
        lplist.append(line.rstrip())
print(lplist)