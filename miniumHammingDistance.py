import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names = ['word', 'bin'])

min = hamming(df.iloc[1,1], df.iloc[2,1])
count = 1;
for i in range(0,100):
	for j in range(0,100):
		if i < j:
			hd = hamming(df.iloc[i,1],df.iloc[j,1])
			print(count,"(",df.iloc[i,0],df.iloc[j,0],")hamming_distance: ",hd)
			count = count + 1;
			if min > hd:
				min = hd

print("min hamming distance", min)

