import pandas as pd
import numpy as np
from numpy.random import default_rng

# Seed for random data
rng = default_rng(12345)

# Generate random data
diff_data = rng.normal(0, 1, 100)

cumulative = np.add.accumulate(diff_data)

# Create Series
data_series = pd.Series(diff_data, name="Diff Data")

# Print Data Series
print(data_series)

# Create DataFrame
data_frame = pd.DataFrame({"DiffS": data_series, "Cumulative": data_series.cumsum()})

# Print Data Frame
print(data_frame)