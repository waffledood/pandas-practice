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


''' Question 6 ''' # my solution gave the wrong answer
pd.Series( [x for x in ser1 if x not in ser2] )


''' Question 7 '''
s = ser1[~ser1.isin(ser2)].tolist() + ser2[~ser2.isin(ser1)].tolist()
pd.Series(s)


''' Question 8 '''
q_25 = ser.quantile(0.25)
q_75 = ser.quantile(0.75)
med_val = ser.median()
max_val = ser.max()


''' Question 9 '''
ser.value_counts()


''' Question 10 ''' # couldn't solve it
s = ser.value_counts()
s.head(2).append(s)


''' Question 11 ''' # my solution gave the wrong answer
pd.qcut(ser, 10, labels=['1st','2nd','3rd','4th','5th','6th','7th','8th', '9th', '10th'])


''' Question 12 '''
pd.DataFrame(ser.values.reshape(7,5))
# link that was helpful https://stackoverflow.com/questions/14390224/reshape-of-pandas-series


''' Question 13 '''
ser[ser % 3 == 0].index 


''' Question 14 '''
ser.loc[pos] 


''' Question 15 '''
pd.concat([ser1, ser2], axis=1)


''' Question 16 ''' # wrong answer
np.argwhere(ser1.isin(ser2))


''' Question 17 '''
((truth - pred) ** 2).mean()
# link that was helpful https://stackoverflow.com/questions/41328922/python-pandas-simple-example-of-calculating-rmse-from-data-frame


''' Question 18 '''
f = lambda a: a.capitalize()
ser.map(f)
# use of lambda: https://www.w3schools.com/python/python_lambda.asp
# use of map() for pandas: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html 


''' Question 19 '''
f = lambda a: len(a)
ser.map(f)


''' Question 20 '''
ser.diff().diff()
# link that was helpful, this applies to Series https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html
# not to be confused with the one for DataFrame https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.diff.html 
