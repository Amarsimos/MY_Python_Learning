magicians = ['alice', 'david', 'carolina']
great_magicians = []

def show_magicians(magicians):
    if magicians:
        for magician in magicians:
            print(magician)
    else:
        print("There are no magicians.")

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magicians.insert(0,'The Great ' + magician)
    return great_magicians

great_magicians = make_great(magicians)
show_magicians(great_magicians)
show_magicians(magicians)