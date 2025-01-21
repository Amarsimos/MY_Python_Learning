citise = {
    'Tokyo':{
        'Country':'Japan',
        'Population':'200000000',
        'Fact':'It\'s a big city'
        },
    'Osaka':{
        'Country':'Japan',
        'Population':'100000000',
        'Fact':'It\'s a middle city'
        },
    'Sapporo':{
        'Country':'Japan',
        'Population':'400000000',
        'Fact':'It\'s a small city'
        }
    }

for city,info in citise.items():
    print(city + ' belongs to ' + info['Country'])
    print('it has a population of',info['Population'])
    print(info['Fact'])