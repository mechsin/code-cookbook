#!/usr/bin/env python3


# Chris Nyland
# 2022-01-09

# Look at an efficient algorithm for calculating a moving average
# by instead using and exponential moving average. This is 
# advantagous because we don't have to keep all the past values.
# Original idea comes from this stack post
# https://stackoverflow.com/questions/10990618/calculate-rolling-moving-average-in-c

# The alpha value controls how far back the look up goes back
# it is a value between zero and one

from statistics import mean
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

def exponential_moving_average(alpha, data):
    avg = 0
    emv = []
    for val in data:
        avg = (alpha * val) + (1 - alpha) * avg
        emv.append(avg)
    emv = np.array(emv[window_size-1:])
    return emv
  
def loss(alpha, data, target):
    emv = exponential_moving_average(alpha, data)  
    return np.linalg.norm(target - emv, 1) 


alpha = 0.13
target = 10

samplesize = 10000

X = list(range(samplesize))
Xval = X
window_size = 100

ns = pd.Series(X)
windows = ns.rolling(window_size)
Y = np.array(windows.mean().tolist()[window_size-1:])

result = minimize_scalar(loss, args=(X,Y))
print(result.x)

print(Y - exponential_moving_average(result.x, X))

np.random.normal(0, .1, samplesize)
