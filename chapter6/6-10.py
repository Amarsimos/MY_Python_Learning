love_num = {'Alice': [10,20,30], 'Bob': [8,39,89], 'Charlie': [12]}
for name,num in love_num.items():
    if len(num) == 1:
        print(name + "'s love numbers is:")
        for n in num:
            print(n)
    else:
        print(name + "'s love numbers are:")
        for n in num:
            print(n)

