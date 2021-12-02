#!/usr/bin/env python3

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

input = np.genfromtxt(r'input') 

slidingWindowSums = np.sum(sliding_window_view(input, window_shape = 3), axis=1)

increasing = np.concatenate([np.array([np.nan]), slidingWindowSums[1:] > slidingWindowSums[:-1]])

print (np.nansum(increasing))