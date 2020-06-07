import time
import numpy as np

"""
with open('gift_costs.txt') as f:
    gift_costs = f.read().split('\n')
""" 
gift_costs = ['1','2','3','4','5']

gift_costs = np.array(gift_costs).astype(int)  # convert string to int

start = time.time()

## normal Code

total_price = 0
for cost in gift_costs:
    if cost < 25:
        total_price += cost * 1.08  # add cost after tax

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

## code Optimization

start = time.time()

print(total_price)
total_price = gift_costs[np.where(gift_costs<25)].sum()*1.08

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))

## code Optimization solution

print(total_price)
total_price = (gift_costs[gift_costs<25)]).sum()*1.08

print(total_price)
print('Duration: {} seconds'.format(time.time() - start))
