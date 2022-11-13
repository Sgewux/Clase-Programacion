import os
import time

from polinomios.operaciones import suma, resta, multiplicacion, division, modulo
from polinomios.utils import pretty_print, leer_polinomio

if __name__ == '__main__':
    menu = {
        1: suma,
        2: resta,
        3: multiplicacion,
        4: division,
        5: modulo
    }

    print('Polinomio 1: ')
    terminos_polinomio_a, grados_polinomio_a = leer_polinomio()
    os.system('cls')
    print('Polinomio 2: ')
    terminos_polinomio_b, grados_polinomio_b = leer_polinomio()
    os.system('cls')

    str_polinomio_a = pretty_print(terminos_polinomio_a, grados_polinomio_a)
    str_polinomio_b = pretty_print(terminos_polinomio_b, grados_polinomio_b)

    while True:
        try:
            print('Que desea hacer con los siguientes polinomios? ')
            print(f'Polinomio 1 = {str_polinomio_a}')
            print(f'Polinomio 2 = {str_polinomio_b}')
            print('='*20)

            for k, v in menu.items():
                print(k, str(v).split(' ')[1])
            
            print('Presione Ctrl + C para salir')
            print('='*20)

            eleccion_usuario = int(input('Operacion a realizar: '))

            resultado = menu[eleccion_usuario](terminos_polinomio_a, grados_polinomio_a, terminos_polinomio_b, grados_polinomio_b)
            resultado = pretty_print(*resultado)

            os.system('cls')
            print(
                f'El resultado de efectuar {str(menu[eleccion_usuario]).split(" ")[1]} entre {str_polinomio_a} y {str_polinomio_b} es = {resultado}'
                )

            time.sleep(5)
            os.system('cls')
        
        except KeyboardInterrupt:
            os.system('cls')
            print('Adios')
            break