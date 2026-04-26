import pygal_maps_world.maps
import pygal

wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in the Americas'

# wm.add('North America',['ca','mx','us'])
wm.add('North America',{'ca':34126000,'mx':113423000,'us':328239523})
wm.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])

wm.render_to_file('americas.svg')