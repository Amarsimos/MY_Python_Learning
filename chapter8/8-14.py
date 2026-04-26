def make_car(maufacturer, model,**more_info):
   car_info = {} 
   car_info['maufacturer'] = maufacturer
   car_info['model'] = model
   for key, value in more_info.items():
      car_info[key] = value
   return car_info

car = make_car('Toyota', 'Camry', color='red', year=2020)
print(car)