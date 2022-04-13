#this is another comment
import math
from fractions import Fraction
from functools import reduce

def modulo(vector):
  sum = 0
  for i in range(len(vector)):
    sum += vector[i]*vector[i]
  raiz = math.sqrt(sum)
  if Fraction(raiz).denominator == 1:
    raiz = int(raiz)
    suma = (1/raiz,'1/'+str(raiz),sum)
  else:
    suma = (1/raiz,'1/√'+str(sum), sum)
  return suma

def multvector(vector, modulo):
  vectorn=[]
  for i in range(len(vector)):
    vectorn.append(vector[i]*modulo)
  return vectorn

def prodintercan(vector1, vector2):
  prodint = 0
  for i in range(len(vector1)):
    prodint += vector1[i]*vector2[i]
  return prodint

def restvector(vector1, vector2):
  vectorn = []
  for i in range(len(vector1)):
    vectorn.append(vector1[i]-vector2[i])
  return vectorn

from functools import reduce
from math import gcd
def find_gcd(list):
    x = reduce(gcd, list)
    return x

def maxcd(vector):
  vectorn = vector
  gcd = find_gcd(vectorn)
  if gcd != 1:
    for i in range(len(vectorn)):
      vectorn[i] = int(vectorn[i]/gcd)
    return vectorn
  return vector
    


def frac(vector):
  vectorn = []
  for i in range(len(vector)):
    vector[i] = round(vector[i],2)
  for i in range(len(vector)):
    if int(Fraction(vector[i]).denominator) !=1:
      denominador = int((Fraction(vector[i]).limit_denominator(10)).denominator)
      for j in range(len(vector)):
        vector[j]=int((Fraction(vector[j]).limit_denominator(10)).numerator)*denominador/((Fraction(vector[j]).limit_denominator(10)).denominator)
    vectorn.append(int(vector[i]))
  return vectorn

campo_reales = int(input("En qué campo de reales está la base: "))
cantidad_vectores = int(input("Digite cantidad de vectores: "))
vectores = []
for i in range(cantidad_vectores):
  vector =[]
  for j in range(campo_reales):
    j = int(input("Digite elemento: "))
    vector.append(j)
  print(vector)
  vectores.append(vector)
print(vectores)

print("\n------ Gram-Schmidt ------\n")

ortonormales = []
ortonormalesmulti= []
ortonormalesvect= []
modulos = []
ortonormalestxt = []
for i in range(cantidad_vectores):
  if i == 0:
    #dividir vector por modulo
    modul = modulo(vectores[i])
    modulos.append(modul[2])
    ortonormal = multvector(vectores[i], modul[0])
    ortonormales.append(ortonormal)
    ortonormalesmulti.append("("+modul[1]+")")
    ortonormalesvect.append(vectores[i])
  else:
    j = i
    zeta = vectores[i]
    while j > 0:
      #imaginando que i=1
      #productointernocanonico
      prodint = prodintercan(vectores[i], ortonormalesvect[j-1])
      #<v1,u0>u0
      prodint = prodint/modulos[j-1]
      operacion = multvector(ortonormalesvect[j-1],prodint)
      #resta v1 - ...
      zeta = restvector(zeta, operacion)
      j-=1
    zeta = frac(zeta)
    mcd = maxcd(zeta)
    modul = modulo(zeta)
    modulos.append(modul[2])
    ortonormal = multvector(zeta, modul[0])
    ortonormales.append(ortonormal)
    ortonormalesmulti.append("("+modul[1]+")")
    ortonormalesvect.append(zeta)

for i in range(len(ortonormalesmulti)):
  ortonormalestxt.append(ortonormalesmulti[i]+str(ortonormalesvect[i]))

print(ortonormalestxt)