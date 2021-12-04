import pandas as pd
from pandasql import sqldf



pd.options.display.max_rows = 10
df = pd.read_csv('../data_act_01.csv', sep = ';')


print(df)
print(df.query(' CrimeId ==  160912801 '))


