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

#   Almacenamos la lista de tipos de crimen, disposiciones y ciudad
#   (estas nos ayudarán a detectar errores a ojo)
listaCrimenes = {}
listaDisposiciones = {}
listaCiudades = {}

#   Por último creamos el dicionario en el cual fijamos el valor de los atributos constantes
dataCrimenesJSON = {
    'State': 'CA',
    'AgencyId': '1'
}

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
        #   state = row['State']
        #   Suprimimos el id de la agencia puesto que es constante para la muestra
        addressType = row['AddressType']


        #   Comprobaciones referentes al tipo de crimen
        crimeType = util.comprobacionTipoCrimen(crimeType,listaCrimenes)
        if crimeType == None:
            shouldAdd = 0

        #   Comprobaciones respecto a la fecha
        array = util.comprobacionFecha(fullDate,hour,date,horaPrevia,fechaPrevia, crimeId)
        if array:
            [fullDate,horaPrevia,fechaPrevia] = array
        else:
            shouldAdd = 0
        #   Debemos quitar la repetición de columnas suprimiendo CallDataTime

        #   Comprobaciones referentes a la disposición
        disposition = util.comprobacionDisposicion(disposition,listaDisposiciones)        

        #   Comprobaciones refentes a la Address
        [address,addressType] = util.comprobacionLugar(address,addressType) or [None,None]
        if not address:
            shouldAdd = 0

        #   Comprobaciones referentes a la ciudad
        ciudad = util.comprobacionCity(city,listaCiudades)
        if not ciudad:
            shouldAdd = 0

        #   Añadimos la fila si corresponde como nueva entrada del diccionario marcada por su id
        if (shouldAdd == 1):
            newRow = {'CallDateTime': fullDate, 'Disposition':disposition, 'Address': address, 'City': ciudad, 'AddressType':addressType}
            dataCrimenesJSON[str(crimeId)] = newRow

        
#   Sacamos por pantalla ambas listas, tipos de crimen y disposición, ordenadas
print(sorted(listaCrimenes.items(), key=lambda x: x[1], reverse=True) )
print(sorted(listaDisposiciones.items(), key=lambda x: x[1], reverse=True) )
print(sorted(listaCiudades.items(), key=lambda x: x[1], reverse=True) )

#   Salvamos el json final en un documento auxiliar
f = open("salvadoCrimenes.txt","w")
f.write(str(dataCrimenesJSON))
f.close()


tiempoEdicion = time.time() - time1
print("El tiempo de edición ha sido {:.5f} seg".format(tiempoEdicion))


    #row.to_csv('../output.csv', mode='a', index=False)

#dff = pd.read_csv('../output.csv', sep = ',')
#print(dff)