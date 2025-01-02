want_go = ['oosaka', 'kyoto', 'nagoya',  'tokyo','aichi']
print('origin:',want_go)
print('\n-----------------')
print('sorted:',sorted(want_go))
print('origin:',want_go)

print('sorted reverse:',sorted(want_go, reverse=True))
print('origin:',want_go)

want_go.reverse()
print('reverse:',want_go)

want_go.reverse()
print('origin:',want_go)

want_go.sort()
print('sort:',want_go)

want_go.sort(reverse=True)
print('sort reverse:',want_go)