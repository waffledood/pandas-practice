'''

Pandas practice!
website link: https://www.machinelearningplus.com/python/101-pandas-exercises-python/

'''

import pandas as pd
import numpy as np 

#Question 7
s = ser1[~ser1.isin(ser2)].tolist() + ser2[~ser2.isin(ser1)].tolist()
pd.Series(s)