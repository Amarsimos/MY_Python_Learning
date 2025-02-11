def make_album(artist,title,tracks = ''):
    if tracks:
        album = {'artist':artist,'title':title,'tracks':tracks}
    else:
        album = {'artist':artist,'title':title}
    return album

album = make_album('Zhangwangao','Python')
print(album)
album = make_album('Zhangwangao','Python','1')
print(album)