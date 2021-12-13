def convertirANuemero(array):
    numero = ""
    for elemento in array:
        numero += str(elemento)
    return int(numero)



def comprobacionFecha(fullDate,hour,date,horaPrevia,fechaPrevia):

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
