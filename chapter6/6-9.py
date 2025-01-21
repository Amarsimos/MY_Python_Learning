fav_place = {"Alice":['Paris', 'London'] , "Bob":['New York', 'San Francisco'], "Charlie": ["London"]}
for name,place in fav_place.items():
    if len(place) == 1:
        print(name, "likes is")
        print(place[0])
    else:
        print(name, "likes places are",)
        for p in place:
            print(p)
