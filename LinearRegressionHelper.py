# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:29:03 2022

@author: Logan
"""

from random import random, uniform

def get_discrete_steps(data_range, scale):
    range_ = []
    for x in range(data_range):
        range_.append(x * scale)
    return range_

def get_random_data(data_range, x_rate, y_rate):
    data_x = []
    data_y = []
    for x in range(data_range):
        data_x.append(random() + (x * x_rate))
        value = uniform(1, -1) + (x * y_rate) + 1
        if value < 0:
            value *= -1
        data_y.append(value)
        
    return data_x, data_y
