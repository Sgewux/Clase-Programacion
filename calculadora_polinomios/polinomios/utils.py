def suma(arr):
  '''
  Recibe como parametro un arreglo de numeros y retorna la suma de los mismos.
  '''
  acumulado = 0
  for i in arr:
    acumulado += i
  return acumulado


def ordenar(arr):
  '''
  Ordena los numeros en el arreglo. Es una implementacion de "qick sort"
  '''
  if len(arr) == 1 or len(arr) == 0:
    return arr
  
  pivote = arr[len(arr)//2]
  menores = [i for i in arr if i<pivote]
  mayores = [i for i in arr if i>pivote]

  return ordenar(menores) + [pivote] + ordenar(mayores)


def ordenar_polinomio(terminos, grados):
  grados_ordenados = ordenar(grados.copy())[::-1]
  terminos_ordenados = []
  for grado in grados_ordenados:
    termino_de_grado = terminos[grados.index(grado)] # El termino al cual  pertenecia ese grado
    terminos_ordenados.append(termino_de_grado)
  
  return terminos_ordenados, grados_ordenados


def encontrar_terminos_de_grado(terminos, grados, grado):
  terminos_de_grado = []
  for i in range(len(terminos)):
    if grados[i] == grado:
      terminos_de_grado.append(terminos[i])
  return terminos_de_grado


def reduccion_de_terminos_semejantes(terminos, grados):
  nuevos_terminos = []
  nuevos_grados = []

  for grado in grados:
    if grado not in nuevos_grados:
      terminos_de_grado = encontrar_terminos_de_grado(terminos, grados, grado)
      operacion = suma(terminos_de_grado)
      if operacion != 0:
        nuevos_terminos.append(operacion)
        nuevos_grados.append(grado)
  
  if nuevos_terminos and nuevos_grados: # Si la reduccion no dio 0
    return ordenar_polinomio(nuevos_terminos, nuevos_grados)
  else:
    return [0], [0]


def pretty_print(terminos, grados):
  polinomio = ''
  for termino, grado in zip(terminos, grados):
    if termino > 0:
      polinomio += '+'
    
    polinomio += str(termino)

    if grado > 1:
      polinomio += 'x^' + str(grado)
    elif grado == 1:
      polinomio += 'x'
  
  return polinomio.strip('+')


def es_divisible(a_grados, b_grados):
  '''
  Retorna True si un polinomio a es divisible por un polinomio b. Polinomios deben estar ordenados
  '''

  return a_grados[0] >= b_grados[0]


def leer_polinomio():
    '''Se encarga de leer un polinomio y organizarlo en la representacion adecuada'''

    grado = int(input('¿De que grado es el polinomio? '))
    terminos = []
    grados = []

    for n in range(grado+1):
        termino = int(input(f'Termino de grado {n}? '))
        terminos.append(termino)
        grados.append(n)

    return ordenar_polinomio(terminos, grados)