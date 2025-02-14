import time
filename = '10-4-guest_book.txt'

flag = True

while flag:
    guest_name = input("Enter your name: ")
    if guest_name == 'q':
        flag = False
    else:
        print("welcome, " + guest_name + "!")
        with open(filename,'a') as guest_book:
            guest_book.write(guest_name + ' visit the guest book on '+ time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print("Thank you for signing the guest book!")
        print("------------------------------------")
        time.sleep(1)

# guest_book_str = ''
# for line in lines:
#     guest_book_str += line.rstrip()
# 
# birthday = input('Enter your birthday (yymmdd): ')
# if birthday in guest_book_str:
#     print('Congratulations! You were born on the day of the first occurrence of the digits of guest_book in the file.')
# else:
#     print('Sorry, you were not born on the day of the first occurrence of the digits of guest_book in the file.')
# 
# print(guest_book_str)
# print(len(guest_book_str))