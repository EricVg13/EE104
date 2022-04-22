# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:36:30 2022

@author: Eric
"""

import math as m
import numpy as np
import scipy.integrate as integ
from scipy import fftpack
from matplotlib import pyplot as plt

############# Generate the signals ################

##### Signal 1 #####
freq1 = 1 # 1Hz
time_step = 0.02
period1 = 1 / freq1
time_vec = np.arange (0,20,time_step)
sig1 = (np.sin(2 * np.pi / period1 * time_vec))


##### Signal 2 #####
freq2 = 10 # 10Hz
period2 = 1 / freq2
sig2 = 0.5 * (np.sin(2 * np.pi / period2 * time_vec))


##### Signal 3 #####
freq3 = 20 # 20Hz
period3 = 1 / freq3
sig3 = 0.5 * (np.sin(2 * np.pi / period3 * time_vec))


##### plot signal combination #####

sig = sig1 + sig2 + sig3
plt.figure(figsize=(60,10))
plt.plot(time_vec, sig, label = 'Low & High Frequency')


############### Compute and plot the power ###########
# The FFT of the signal
sig_fft = fftpack.fft(sig)
 
# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Plot the FFT power
plt.figure(figsize=(60, 10))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')

# Find the peak frequency: we can focus on only the positive frequencies
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]
 

###### Remove all the high frequencies #################
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

plt.figure(figsize=(60, 10))
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=3, label='Filtered signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.legend(loc='best')



############### Re-Compute and plot the power ###########
# The FFT of the signal
sig_fft1 = fftpack.fft(filtered_sig)

# And the power (sig_fft is of complex dtype)
power = np.abs(sig_fft1)**2

# The corresponding frequencies
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

# Plot the FFT power
plt.figure(figsize=(30, 20))
plt.plot(sample_freq, power)
plt.xlabel('Frequency [Hz]')
plt.ylabel('plower')








