import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Unemployment_Rate': [6.1,5.8,5.7,5.7,5.8,5.6,5.5,5.3,5.2,5.2], 
    'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565] 
    } 

df = pd.DataFrame(data,columns=['Unemployment_Rate','Stock_Index_Price'])

df.plot(x ='Unemployment_Rate', y='Stock_Index_Price', kind = 'scatter') 
plt.show()