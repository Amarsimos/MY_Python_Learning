def make_album(artist,title,tracks = ''):
    if tracks:
        album = {'artist':artist,'title':title,'tracks':tracks}
    else:
        album = {'artist':artist,'title':title}
    return album

while True:
    artist = input("Enter the artist name: ")
    if artist == 'q':
        break
    title = input("Enter the album title: ")
    if title == 'q':
        break
    album = make_album(artist,title)
    print(album)