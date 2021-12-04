import pandas as pd
from pandasql import sqldf



pd.options.display.max_rows = 10
df = pd.read_csv('../data_act_01.csv', sep = ';')
print(df)


#print(df)
#print(df.query(' CrimeId ==  160912801 '))

tamañoParte = 10**3 // 2  # you may want to adjust it ... 
for parte in pd.read_csv('../data_act_01.csv', chunksize=tamañoParte, sep= ';'):
    pedazoToTest = parte.query(' CrimeId > 160932801 ')
    pedazoToTest.to_csv('output.csv', mode='a', index=False)

dff = pd.read_csv('output.csv', sep = ',')
print(dff)