import pandas as pd 
import numpy as np 

#creating the DataFrame
df = pd.DataFrame({'a':[0,1,''],'b':['',None,3]}) 

print("------The DataFrame is----------") 
print(df) 
print("---------------------------------") 
print(df.isna())