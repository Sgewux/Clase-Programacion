from .utils import reduccion_de_terminos_semejantes, es_divisible

def suma(a_terminos, a_grados, b_terminos, b_grados):
  coeficientes = a_terminos + b_terminos
  grados = a_grados + b_grados

  return reduccion_de_terminos_semejantes(coeficientes, grados)


def resta(a_terminos, a_grados, b_terminos, b_grados):
  # Cambio de signo
  b_nuevos_terminos = [-1*termino for termino in b_terminos]

  terminos = a_terminos + b_nuevos_terminos
  grados = a_grados + b_grados

  return reduccion_de_terminos_semejantes(terminos, grados)


def multiplicacion(a_terminos, a_grados, b_terminos, b_grados):
  terminos = []
  grados = []
  
  for i in range(len(a_terminos)):
    factor = []
    grados_factor = []
    grado_termino_i = a_grados[i]

    for j in range(len(b_terminos)):
      grado_termino_j = b_grados[j]
      factor.append(a_terminos[i] * b_terminos[j])
      grados_factor.append(grado_termino_i + grado_termino_j)
    
    terminos += factor
    grados += grados_factor


  return reduccion_de_terminos_semejantes(terminos, grados)


def division(a_terminos, a_grados, b_terminos, b_grados):
  terminos_residuo = a_terminos.copy()
  grados_residuo = a_grados.copy()

  terminos_resultado = []
  grados_resultado = []

  while es_divisible(grados_residuo, b_grados):
    nuevo_coeficiente = int(terminos_residuo[0] / b_terminos[0])
    nuevo_grado = grados_residuo[0] - b_grados[0]

    terminos_resultado.append(nuevo_coeficiente)
    grados_resultado.append(nuevo_grado)

    terminos_residuo, grados_residuo = resta(
        terminos_residuo, grados_residuo, *multiplicacion(b_terminos, b_grados, [nuevo_coeficiente], [nuevo_grado])
    )


  return terminos_resultado, grados_resultado


def modulo(a_coeficientes, a_grados, b_coeficientes, b_grados):
  coeficientes_residuo = a_coeficientes.copy()
  grados_residuo = a_grados.copy()

  coeficientes_resultado = []
  grados_resultado = []

  while es_divisible(grados_residuo, b_grados):
    nuevo_coeficiente = int(coeficientes_residuo[0] / b_coeficientes[0])
    nuevo_grado = grados_residuo[0] - b_grados[0]

    coeficientes_resultado.append(nuevo_coeficiente)
    grados_resultado.append(nuevo_grado)

    coeficientes_residuo, grados_residuo = resta(
        coeficientes_residuo, grados_residuo, *multiplicacion(b_coeficientes, b_grados, [nuevo_coeficiente], [nuevo_grado])
    )


  return coeficientes_residuo, grados_residuo