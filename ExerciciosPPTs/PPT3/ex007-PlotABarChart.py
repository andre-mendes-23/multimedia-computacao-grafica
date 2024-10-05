import pandas as pd 
import matplotlib.pyplot as plt 
data = {
    'Country': ['USA','Canada','Germany','UK','France'], 
    'GDP_Per_Capita': [45000,42000,52000,49000,47000] 
    } 

df = pd.DataFrame(data,columns=['Country','GDP_Per_Capita']) 
df.plot(x ='Country', y='GDP_Per_Capita', kind = 'bar') 
plt.show()