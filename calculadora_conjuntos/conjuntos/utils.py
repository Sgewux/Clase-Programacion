from .errores import ErrorElementoRepetido

def leer_conjunto():
    tamano = int(input('De cuantos elementos va a ser el conjunto? '))
    conjunto = []
    for i in range(1, tamano+1):
        elemento = int(input(f'Elemento {i}: '))
        if elemento not in conjunto: # Aun no ha añadido ese elemento al conjunto
            conjunto.append(elemento)
        else:
            raise ErrorElementoRepetido(elemento)
    return conjunto