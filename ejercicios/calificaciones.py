calificaciones=[20,40,60,80,90]
resultados=sum(calificaciones)/len(calificaciones)
print(f"{resultados:.0f}")


def calcularAreaCuadrado(base,altura):
    #print(base*altura)
    return base*altura

nuemroA=int(input())

nuemroB=int(input())

print(calcularAreaCuadrado(nuemroA,nuemroB))
