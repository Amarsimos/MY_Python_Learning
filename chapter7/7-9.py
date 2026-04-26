sandwich_orders = ['ham', 'turkey','beef','pastrami', 'pastrami','pastrami']
finished_sandwiches = []
print('Out of pasrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)