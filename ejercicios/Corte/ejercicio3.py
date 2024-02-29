import datetime

fechaActual=datetime.datetime.now()
actualYear=int(fechaActual.strftime('%Y'))
yearI=int(input('Indique año de nacimiento: '))
print(actualYear-yearI, "es su edad estimada")
