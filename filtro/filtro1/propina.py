#programa para calcular propinas
totalCuentaRestaurante=int(input("total de la cuenta en restaurante: "))
propinaPorcentaje=1.12 #esto serai el 12% dentro de una formula matematica
#razon de la formula x(1+%n)= x*1.n)
totalMasPropina=totalCuentaRestaurante*propinaPorcentaje
print("Total de la cuenta + 12% "+ "en propina:", totalMasPropina)#espaciado para evitar que tome el % e como formato