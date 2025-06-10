import pandas as pd

df = pd.read_csv('Data').set_index('State')
states = list(df.index.unique())
states.insert(0,'All States')

attributtes_ = df.columns[4:]