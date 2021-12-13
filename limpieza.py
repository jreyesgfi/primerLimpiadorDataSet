import pandas as pd
from pandasql import sqldf
import time
import util


time1 = time.time()
pd.options.display.max_rows = 10
df = pd.read_csv('../data_act_01.csv', sep = ';')
print(df)
tiempoLectura = time.time() - time1
print("El tiempo de lectura ha sido {:.5f} seg".format(tiempoLectura))


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
newData['FullDate'] = None
newData['Disposition'] = None
newData['Address'] = None
newData['City'] = None
newData['AddressType'] = None

#   Separamos el dataframe en filas
time1 = time.time()

#   Almacenamos la fecha previa para asegurarnos que van en orden
fechaPrevia = 20160330
horaPrevia = 1842

#   Almacenamos la lista de tipos de crimen
listaCrimenes = {}

for index, row in df.iterrows(): # De esta manera se abrirá como un objeto

    if (row['CrimeId']> 0.160954249):

        #   Booleano para decidir si añadimos columna
        shouldAdd = 1

        crimeId = row['CrimeId'] 
        crimeType = row['OriginalCrimeTypeName']
        date = row['OffenseDate']
        hour = row['CallTime']
        fullDate = row['CallDateTime']
        disposition = row['Disposition']
        address = row['Address']
        city = row['City']
        state = row['State']
        #   Suprimimos el id de la agencia puesto que es constante para la muestra
        addressType = row['AddressType']


        #   Comprobaciones referentes al tipo de crimen
        crimeType = util.comprobacionTipoCrimen(crimeType,listaCrimenes)
        if crimeType == None:
            shouldAdd = 0

        #   Debemos quitar la repetición de columnas suprimiendo CallDataTime, aunque estaría bien comprobar si todos los datos son iguales
        #   Comprobaciones respecto a la fecha
        [fullDate,horaPrevia,fechaPrevia] = util.comprobacionFecha(fullDate,hour,date,horaPrevia,fechaPrevia)

        #   Comprobaciones referentes a la disposición
        if (len(disposition) !=3): # disposition == 'Not recorded'
            shouldAdd = 0

        #   Comprobaciones refentes a la Address
        [address,addressType] = util.comprobacionLugar(address,addressType)
        


        #   Añadimos la fila si corresponde
        if (shouldAdd == 1):
            newRow = pd.Series([crimeId, crimeType, fullDate, disposition, address, city, addressType], index = newData.columns )
            newData = newData.append(newRow, ignore_index = True)


print(sorted(listaCrimenes.items(), key=lambda x: x[1], reverse=True) )
tiempoEdicion = time.time() - time1
print("El tiempo de edición ha sido {:.5f} seg".format(tiempoEdicion))


    #row.to_csv('../output.csv', mode='a', index=False)

#dff = pd.read_csv('../output.csv', sep = ',')
#print(dff)