number = list(range(1,10))
for i in number:
    if i == 1:
        print('1st')
    elif i == 2:
        print('2nd')
    elif i == 3:
        print('3rd')
    else:
        print(str(i)+"th")
        # 如果变量 i 的类型不是字符串，例如是整数类型，那么在进行字符串连接时会抛出 TypeError。为了避免这个问题，可以使用 str(i) 将 i 转换为字符串
