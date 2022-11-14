import os
import time

from conjuntos.utils import leer_conjunto
from conjuntos.errores import ErrorElementoRepetido
from conjuntos.operaciones import union, interseccion, diferencia, diferencia_simetrica, pertenece, contenido

if __name__ == '__main__':
    menu = {
        1: union,
        2: interseccion,
        3: diferencia,
        4: diferencia_simetrica,
        5: pertenece,
        6: contenido
    }

    try:
        print('Conjunto A ')
        a = leer_conjunto()
        os.system('cls')
        print('Conjunto B ')
        b = leer_conjunto()
        os.system('cls')
    
    except ErrorElementoRepetido as e:
        os.system('cls')
        print(e)
    
    while True:
        try:
            print('Que desea hacer con los siguientes conjuntos?')
            print(f'A = {a}')
            print(f'B = {b}')

            for k, v in menu.items():
                print(k, str(v).split(' ')[1])
            
            print('Presione Ctrl + C para salir')
            print('='*20)
            
            eleccion_usuario = int(input('Operacion a realizar: '))

            if eleccion_usuario == 5:
                n = int(input('Que numero? '))
                conjunto = input('A que conjunto? (A,B) ').upper()

                resultado = menu[eleccion_usuario](n, a if conjunto=='A' else b)
                
                os.system('cls')

                if resultado:
                    print(f'{n} si pertenece a {conjunto}')
                else:
                    print(f'{n} no pertenece a {conjunto}')
                    
            else:
                resultado = menu[eleccion_usuario](a,b)

                os.system('cls')
                print(
                    f'El resultado de efectuar {str(menu[eleccion_usuario]).split(" ")[1]} entre {a} y {b} es = {resultado}'
                )

            time.sleep(5)
            os.system('cls')

        except KeyboardInterrupt:
            os.system('cls')
            print('Adios')
            break

    


