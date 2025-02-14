filename = '10-3-guest.txt'

guest_name = input("Enter your name: \n")

with open(filename,'a') as guest:
    guest.write(guest_name + '\n')
    # lines = guest.readlines()

# guest_str = ''
# for line in lines:
#     guest_str += line.rstrip()
# 
# birthday = input('Enter your birthday (yymmdd): ')
# if birthday in guest_str:
#     print('Congratulations! You were born on the day of the first occurrence of the digits of guest in the file.')
# else:
#     print('Sorry, you were not born on the day of the first occurrence of the digits of guest in the file.')
# 
# print(guest_str)
# print(len(guest_str))