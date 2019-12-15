#-*- coding: utf8 -*-

import os
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Generate histogram with campaign frequencies
"""

# Receives the filepath as argument
source = sys.argv[1]

df = pd.read_csv(source, header=0, usecols=['campaign', 'y'])
campaigns = df['campaign'].tolist()
result = df['y'].tolist()

campaign_y = [x for i, x in enumerate(campaigns) if result[i] == 'yes']
campaign_n = [x for i, x in enumerate(campaigns) if result[i] == 'no']

# The data is not balanced (521 positive vs 4000 negative)
campaign_y = (campaign_y.copy() + campaign_y.copy() + campaign_y.copy() + campaign_y.copy()
    + campaign_y.copy() + campaign_y.copy() + campaign_y.copy() + campaign_y.copy()
    + campaign_y.copy() + campaign_y.copy() + campaign_y.copy() + campaign_y.copy()
    + campaign_y.copy() + campaign_y.copy() + campaign_y.copy())

n, bins, patches = plt.hist(x = campaign_n, bins = 'auto', alpha = 0.7, rwidth = 0.85)
plt.hist(x = campaign_y, bins = bins, alpha = 0.7, rwidth = 0.85)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel('Campaign')
plt.ylabel('Frequency')
plt.title('Histogram of campaigns')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax = np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

