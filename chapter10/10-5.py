import time
filename = '10-5-reason.txt'

flag = True

while flag:
    question = input("why you like Python? (q to quit) ")
    if question == 'q':
        flag = False
    else:
        with open(filename,'a') as reason:
            reason.write(question + '\n')
        print("Thank you for answering!")
        print("------------------------------------")
        time.sleep(1)

# reason_str = ''
# for line in lines:
#     reason_str += line.rstrip()
# 
# birthday = input('Enter your birthday (yymmdd): ')
# if birthday in reason_str:
#     print('Congratulations! You were born on the day of the first occurrence of the digits of reason in the file.')
# else:
#     print('Sorry, you were not born on the day of the first occurrence of the digits of reason in the file.')
# 
# print(reason_str)
# print(len(reason_str))