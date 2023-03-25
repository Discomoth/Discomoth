
import allantools
from matplotlib import pyplot as pl
import numpy as np
import os
import sys

frequencyDataFile = os.path.dirname(os.path.abspath(__file__)) + '/output.txt'

with open(frequencyDataFile, 'r') as dataFile:
    freqData = [float(data.strip()) for data in dataFile.readlines()]

#print(freqData)

tauValues = np.linspace(0, 1000, 2000)
sampleRate = 1

(t2, ad, ade, adn) = allantools.oadev(freqData, rate=sampleRate, data_type='freq', taus=tauValues)

pl.plot(t2, ad)
pl.xscale('log')
pl.yscale('log')
pl.show()