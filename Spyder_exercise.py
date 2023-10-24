# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:38:52 2023

@author: Paula Hugo
"""
#import
import numpy as np

#importmatplot
import matplotlib.pyplot as plt 

#import pandas
import pandas as pd

#create dataframe
barc = pd.read_csv('BCS_ann.csv')
tes = pd.read_csv('TSCO_ann.csv')
bp = pd.read_csv('BP_ann.csv')
vod = pd.read_csv('VOD_ann.csv')
print(barc, tes, bp, vod)

plt.figure()
plt.subplot(2, 2, 1)
plt.hist(barc["ann_return"], label="BARCALAYS", color = "red")
plt.legend()

plt.subplot(2, 2, 2)
hist2 = plt.hist(tes["ann_return"], label="TESCO", color = "magenta")
plt.legend()

plt.subplot(2, 2, 3)
hist3 = plt.hist(bp["ann_return"], label="BP", color = "black")
plt.legend()

plt.subplot(2, 2, 4)
hist4 = plt.hist(vod["ann_return"], label="VODAPHONE")
plt.legend()

plt.show()
