def city_funs(city, country,population=' '):
    if population:
        return (f"{city},{country}-population {population}")
    else:
        return (f"{city},{country}")
