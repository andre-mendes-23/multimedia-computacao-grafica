import pandas as pd
import numpy as np
from numpy.random import default_rng

df = pd.DataFrame({'A': [1,2,3], 'B': [10,20,30]})

def plus_10(x):
    return x + 10

df.apply(plus_10)


print(df)