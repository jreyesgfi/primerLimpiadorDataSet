def convertirANuemero(array):
    numero = ""
    for elemento in array:
        numero += str(elemento)
    return int(numero)



def comprobacionFecha(fullDate,hour,date,horaPrevia,fechaPrevia):

    # Estructuramos hora y fecha
    [fecha,hora] = fullDate.split('T')
    if (hora[0] == '0'):
        hora = hora[1:]

    hora2 = hour + ':00'
    if (hora != hora2):
        #print(hora, hora2, 'Anteriores horas ')

        # Comprobamos cual de las dos es más similar a la anterior
        dif1 = convertirANuemero( hora.split(':') ) - horaPrevia
        dif2 = convertirANuemero( hora2.split(':') ) - horaPrevia

        # Comparamos las diferencias en valor absoluto (equivalentemente cuadrados)
        if dif2**2 < dif1**2:
            hora = hora2
            dif1 = dif2
            
        

    fecha2 = date.split('T')[0]
    if (fecha != fecha2):

        #print(fecha, fecha2, 'Anteriores fechas ')

        # Si tienen diferentes fechas separamos año mes y dia y operamos igual que la hora
        dif1 = convertirANuemero( fecha.split('-') ) - fechaPrevia
        dif2 = convertirANuemero( fecha2.split('-') ) - fechaPrevia

        if dif2**2 < dif1**2:
            fecha = fecha2
            dif1 = dif2

    # Ajustamos los valores previos
    horaPrevia = convertirANuemero( hora.split(':') )
    fechaPrevia = convertirANuemero( fecha.split('-') )
     
    # Construimos la nueva fecha
    fullDate = str(fecha) +"T"+ str(hora)

    return [fullDate,horaPrevia,fechaPrevia]


def comprobacionLugar(address, addressType,):
    errorWithBlock = address.find('Blk')
    cambiarAddress = False
    if (errorWithBlock != -1):
        #   Pasamos de blk -> block
        address = address[:(errorWithBlock + 2)] + 'oc' + address[(errorWithBlock + 2):]
        cambiarAddress = True
        
    #   Comprobaciones referentes al addresstype
    tiposAddressPermitidos = ['Premise Address', 'Intersection', 'Geo-Override','Common Location','']

    #   Si hay un fallo en la escritura le atribuimos automáticamente la etiqueta
    if (addressType not in tiposAddressPermitidos):
        print(address, addressType)
        cambiarAddress = True

    #   Comprobamos que cuadren las etiqutas respecto a la condición de intersección
    if '/' in address:
        addressType = 'Intersection'
    else:
        if (addressType == 'Intersection'):
            cambiarAddress = True

    #   Si hay que ajustar el addresstype lo hacemos
    if cambiarAddress == True:
        if ('/' in address):
                addressType = 'Intersection'
                print(address, addressType)
        else:
            addressType = 'Premise Address'

    #   Se debería comprobar si los geo-override son sitios reales
    return [address,addressType]
    