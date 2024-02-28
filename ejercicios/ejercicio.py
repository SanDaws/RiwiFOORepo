def pruebas():
    ArrayA=['Paris','Italia','Grecia']
    ArrayB=['Alemania','Paris','Turquia','España']
    print(min(len(ArrayA),len(ArrayB)))
    Resul=[i for i in ArrayA if i in ArrayB]
    print(Resul)


"""
Ejercicio:
Dada una lista de nombre en mayuscula y minuscula ordenar alfabeticamente, ignorando mayusculas y minusculas
"""

listaNombrtes=['alberto','Pedro','Ricardo','Maria','Carolina']
listaNombrtes.sort(key=str.casefold)
print(*listaNombrtes)
