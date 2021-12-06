import pandas as pd
from pandasql import sqldf



pd.options.display.max_rows = 10
df = pd.read_csv('../data_act_01.csv', sep = ';')
print(df)


#print(df)
#print(df.query(' CrimeId ==  160912801 '))

#tamañoParte = 1
#for row in pd.read_csv('../data_act_01.csv', chunksize=tamañoParte, sep= ';'):

    #pedazoToTest = parte.query(' CrimeId > 160932801 ')
    #if (row[0]['CrimeId'] == 160964227):
    #    print(row[0]['OriginalCrimeTypeName'])



#   Creamos la estructura del nuevo dataframe
newData = pd.DataFrame()
newData['CrimeId'] = None
newData['OriginalCrimeTypeName'] = None
newData['Disposition'] = None
newData['Address'] = None
newData['City'] = None
newData['AddressType'] = None

#   Separamos el dataframe en filas

for index, row in df.iterrows():
    if (row['CrimeId']> 160954249):
        #   Leemos la información anterior y la almacenamos en una variable temporal
        crimeId = row['CrimeId']
        originalCrimeType = row['OriginalCrimeTypeName']
        disposition = row['Disposition']
        address = row['Address']
        city = row['City']
        addressType = row['AddressType']


        #   Debemos quitar la repetición de columnas suprimiendo CallDataTime, aunque estaría bien comprobar si todos los datos son iguales
        [fecha,hora] = row['CallDateTime'].split('T')
        if (hora[0] == '0'):
            hora = hora[1:]
        hora2 = row['CallTime'] + ':00'
        if (hora != hora2):
            print(row['CrimeId'], "Tiene diferentes horas...")

        newRow = pd.Series([crimeId, originalCrimeType, disposition, address, city, addressType], index = newData.columns )
        newData = newData.append(newRow, ignore_index = True)

print(newData)

    #row.to_csv('../output.csv', mode='a', index=False)

#dff = pd.read_csv('../output.csv', sep = ',')
#print(dff)