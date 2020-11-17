'''

Pandas practice!
website link: https://www.machinelearningplus.com/python/101-pandas-exercises-python/

further solutions & details found on my Notion!

'''

import pandas as pd
import numpy as np 

''' Question 1 ''' # incomplete answer
import pandas as pd


''' Question 2 '''
pd.Series(mylist)
pd.Series(myarr)
pd.Series(mydict)


''' Question 3 '''
pd.DataFrame(ser).reset_index()


''' Question 4 '''
# Solution 1
s = [ser1, ser2]
pd.DataFrame(s).transpose()

# Solution 2
s = ser1.to_list() + ser2.to_list()
pd.DataFrame(s)


''' Question 5 '''
ser.rename('alphabets', inplace=True)


''' Question 6 ''' #(my solution gave the wrong answer)
pd.Series( [x for x in ser1 if x not in ser2] )


''' Question 7 '''
s = ser1[~ser1.isin(ser2)].tolist() + ser2[~ser2.isin(ser1)].tolist()
pd.Series(s)


''' Question 8 '''
q_25 = ser.quantile(0.25)
q_75 = ser.quantile(0.75)
med = ser.median()
max = ser.max()