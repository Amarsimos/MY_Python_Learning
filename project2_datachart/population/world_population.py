import json

filename = 'Population.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict_country in pop_data.items():
    for name,data in  pop_dict_country.items():
        for year in data.items():
    # for pop_dict_key in {pop_dict_country}:
            print(year)
#         if pop_dict_key == '2015':
#             country_name =pop_dict['Country Name']
#             population = pop_dict['Value']
#         print(country_name + ":" + population)
    # print(pop_data)