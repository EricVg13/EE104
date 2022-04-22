# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:02:14 2022

@author: Eric
"""
## https://www.kaggle.com/kinguistics/heartbeat-sounds
## https://www.kaggle.com/code/mychen76/heart-sounds-analysis-and-classification-with-lstm

import math as m
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt
import heartpy as hp

sample_rate = 500


data = hp.get_data('HB_2nd_filtered_Output_mono.csv')
#data = hp.get_data('data.csv')

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

# run analysis
wd, m = hp.process(data, sample_rate)

# Visualize in plot of custom size   
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

# #display computed measures
# for measure in m.keys():
#     print('%s: %f' %(measure, m[measure]))
