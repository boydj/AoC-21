#!/usr/bin/env python3

import numpy as np

input = np.genfromtxt(r'input') 

increasing = np.concatenate([np.array([np.nan]), input[1:] > input[:-1]])

print (np.nansum(increasing))