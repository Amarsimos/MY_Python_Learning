import json
from country_code import get_country_code
import pygal_maps_world.maps

filename = 'Population.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict_country ,pop_dict_value in pop_data.items():
    try :
        for key,value in  pop_dict_value.items():
            if key == 'name':
                code = get_country_code(value)
            if key == 'data':
                for year,data in value.items():
                    if year == '2100':
                        population = data
                        country_name = pop_dict_value['name']
                        print(country_name + ':' + str(population))

                        if code:
                            cc_populations[code] = population
                            # print(code +":" + str(population))
                        else:
                            print('ERROR -' + country_name)
    except:
        print(pop_dict_country + ':' + str(pop_dict_value))

wm = pygal_maps_world.maps.World()
wm.title = "World Population in 2100, by Country"
wm.add('2100',cc_populations)

wm.render_to_file('world_population.svg')
        # for year,data in value.items():
        # for year in data.items():
    # for pop_dict_key in {pop_dict_country}:
#         if pop_dict_key == '2015':
#         print(country_name + ":" + population)
    # print(pop_data)