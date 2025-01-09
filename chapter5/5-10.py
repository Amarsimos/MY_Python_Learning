current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
new_users = ['Frank', 'Grace', 'Henry', 'DAvid', 'Eve']
for user in new_users:
    # if user.lower() in current_users:
    # 程序遍历每个新用户 new_users，并使用列表推导式将 current_users 中的用户名转换为小写形式进行比较。
    if user.lower() in [user.lower() for user in current_users]:
        print(user,"is already in the list.Add another name.")
    else:
        print(user,"is not in the list.")