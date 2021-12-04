import pandas as pd

pd.options.display.max_rows = 10
df = pd.read_csv('../data_act_01.csv')


print(df.to_string()) 