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
    for magician in magicians:
        great_magicians.append('The Great ' + magician)
    return great_magicians

great_magicians = make_great(magicians)
print("Great magicians:")
show_magicians(great_magicians)
print("Original magicians:")
show_magicians(magicians)