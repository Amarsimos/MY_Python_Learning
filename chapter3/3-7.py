want_people = ['Jay Chou,','Steven Chou,','Kutoushinichi,','Hatoriheiji,']
letter = 'Dear ' + want_people[0] + want_people[1] + want_people[2] + want_people[3] + '\n\nI am writing to invite you to attend a wedding ceremony on April 1st.\nPlease let me know if you have any questions or concerns.\n\nThank you for your consideration.\n\nBest regards,\n\nAmarsimos'
print(letter)
print('1---------------------------------------------')
message = 'Sorry to hear that '+ want_people[3]+'can not make it to the wedding. We will try to find another date for you.'
print(message)
print('---------------------------------------------')
want_people[3] = 'kaidoukitto,'
message1 = 'But we found a new person for the wedding who is ' + want_people[3]
print(message1)
letter = 'Dear ' + want_people[0] + want_people[1] + want_people[2] + want_people[3] + '\n\nI am writing to invite you to attend a wedding ceremony on April 1st.\nPlease let me know if you have any questions or concerns.\n\nThank you for your consideration.\n\nBest regards,\n\nAmarsimos'
print('---------------------------------------------\n'+letter)#在 Python 中，如果你是在字符串中直接使用 want_people[3] 的值，那么即使之后更新了列表里的内容，之前生成的字符串值不会改变。因此，letter 中仍然会显示原始的值。
print('---------------------------------------------')
message2 = 'We just found a bigger dinner table for the wedding. We will invite more people to join us.'
print(message2)
want_people.insert(0,'mourikogorou,')
want_people.insert(2,'yukinohara,')
want_people.append('mouriran,')
letter = 'Dear ' + ' '.join(want_people) + '\n\nI am writing to invite you to attend a wedding ceremony on April 1st.\nPlease let me know if you have any questions or concerns.\n\nThank you for your consideration.\n\nBest regards,\n\nAmarsimos'
print('---------------------------------------------\n'+letter)
print('----------------------------------------------')
message3 = 'We are sorry to inform you that our new table can not reach the wedding date. We will only invite 2 people to join us.' 
print(message3)
excluded_person = want_people.pop()
message4 = 'We have excluded ' + excluded_person +'from the invitation.'
print(message4)
excluded_person = want_people.pop()
message4 = 'We have excluded ' + excluded_person +'from the invitation.'
print(message4)
excluded_person = want_people.pop()
message4 = 'We have excluded ' + excluded_person +'from the invitation.'
print(message4)
excluded_person = want_people.pop()
message4 = 'We have excluded ' + excluded_person +'from the invitation.'
print(message4)
excluded_person = want_people.pop()
message4 = 'We have excluded ' + excluded_person +'from the invitation.'
print(message4)
print('now the list is:',want_people)
print('----------------------------------------------')
message5 = 'And ' + want_people[0] + 'will be the one of the person invited to the wedding.'
print(message5)
message5 = 'And ' + want_people[1] + 'will be the one of the person invited to the wedding.'
print(message5)
print('----------------------------------------------')
del want_people[1]
del want_people[0]

print('now the list is:',want_people)