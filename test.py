import pandas as pd
import numpy as np
my_di = {'name': ['Jiya','Tim','Rohan'],
         'age': np.array([10,15,20]),
         'weight':(75,123,239),
         'height':[4.5,5,6.1],
         'siblings':1,
         'gender':'M'}
df = pd.DataFrame(my_di,index=my_di['name'])
df['IQ']=[130,105,115]
df['Married']=False
print(df)
