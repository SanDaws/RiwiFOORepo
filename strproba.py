       #          1
       #0123456789012345678
cadena="3WizarsdJumpToFight"
vocals="AEIOUaeiou"


def solucion(cadena,vocales):
    return sum(cadena.count(vocal) for vocal in vocales )

print(solucion(cadena,vocals))
