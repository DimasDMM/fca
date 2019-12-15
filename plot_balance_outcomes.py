#-*- coding: utf8 -*-

import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Generate histogram with outcomes based on balances
"""

# Receives the filepath as argument
source = sys.argv[1]

df = pd.read_csv(source, header=0, usecols=['balance', 'y'])
balance = df['balance'].tolist()
result = df['y'].tolist()

balance_y = [x for i, x in enumerate(balance) if result[i] == 'yes']
balance_n = [x for i, x in enumerate(balance) if result[i] == 'no']

n, bins, patches = plt.hist(x = balance_n, bins = 'auto', alpha = 0.7, rwidth = 0.85)
plt.hist(x = balance_y, bins = bins, alpha = 0.7, rwidth = 0.85)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Balance')
plt.ylabel('Frequency')
plt.title('Histogram of balance')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax = np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()
