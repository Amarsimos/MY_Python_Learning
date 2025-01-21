reseive_peoples_name  = ('John', 'Edward','jen',)
favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
     }

for name in favorite_languages.keys():
    #这一行代码试图将一个字符串（name.lower()）与一个列表（[names.lower() for names in reseive_peoples_name]）进行比较。
    #if name.lower() == [names.lower() for names in reseive_peoples_name]:
    if name.lower() in [names.lower() for names in reseive_peoples_name]:
        print('Thanks for entering your name.' + name.title())
    else:
        print('Could you please enter your name in lowercase?' + name.title())
        
print('-------------------------')
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")