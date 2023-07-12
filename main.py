import pandas as pd
import numpy as np

train = pd.read_csv("data/train.csv")
pd.options.display.max_columns = train.shape[1]
print(train.shape)
