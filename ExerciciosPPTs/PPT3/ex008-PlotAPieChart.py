import pandas as pd 
import matplotlib.pyplot as plt

data = {'Tasks': [300,500,700]} 

df = pd.DataFrame(data,columns=['Tasks'],index= ['Tasks Pending','Tasks Ongoing','Tasks Completed'])

df.plot.pie(y='Tasks',figsize=(5,5),autopct='%1.1f%%', startangle=90) 

plt.show()