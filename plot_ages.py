#-*- coding: utf8 -*-

import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Generate histogram with age frequencies
"""

# Receives the filepath as argument
source = sys.argv[1]

df = pd.read_csv(source, header=0, usecols=['age'])
ages = df['age'].tolist()

n, bins, patches = plt.hist(x = ages, bins = 'auto', color = '#0504aa',
                            alpha = 0.7, rwidth = 0.85)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of ages')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax = np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

