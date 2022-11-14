def union(a, b):
  u = []
  for elemento in a+b:
    if elemento not in u:
      u.append(elemento)
  return u



def interseccion(a,b):
  en_comun = []

  for elemento in a:
    if elemento in b:
      en_comun.append(elemento)
  return en_comun


def diferencia(a,b):
  '''
  La diferencia del conjunto A menos B, denotado por A – B, es el conjunto formado por los elementos que estén en A y no en B
  '''
  diferentes = []
  for elemento in a:
    if elemento not in b:
      diferentes.append(elemento)
  return diferentes


def diferencia_simetrica(a,b):
  return union(diferencia(a,b), diferencia(b,a))


def pertenece(n, a):
  return n in a


def contenido(a,b):
  '''
  Determina si el conjunto a está contenido en el conjunto b
  '''
  for elemento in a:
    if elemento not in b:
      return False
  
  return True