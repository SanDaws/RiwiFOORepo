import datetime


actualYear=int(datetime.datetime.today().year)
yearI=int(input('Indique año de nacimiento: '))
print(actualYear-yearI, "es su edad estimada")
