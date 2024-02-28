import datetime
HoraActual= datetime.datetime.now()
print(HoraActual)
horaP8=datetime.time.hour(8)
horaAlarma=HoraActual.hour()+horaP8

print(horaAlarma)