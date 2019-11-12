
import csv

# Ejercicio 1
a = range(50)
print(list(range(1, 51)))

# Ejercicio 2

x = range(200)
print(list(range(2, 202, 2)))

# Ejercicio 3
import random
import numpy as np


def listaAleatorios(n):
    lista = [0] * n
    for i in range(n):
        lista[i] = random.random()
    return lista


a = listaAleatorios(4)
b = listaAleatorios(4)
c = listaAleatorios(4)
d = listaAleatorios(4)
e = listaAleatorios(4)
f = listaAleatorios(4)
g = listaAleatorios(4)
h = listaAleatorios(4)
j = listaAleatorios(4)
k = listaAleatorios(4)

all = [a, b, c, d, e, f, g, h, j, k]
print(np.array(all))

# Ejercicio 4

for e in all:
    for e1 in e:
        if e1 >= 0.5:
            print("Estos son los numeros iguales o mayoraes a", "=", e1)

# Ejercicio 5

b = np.array([[[0.55867166, 0.06210792, 0.08147297],
               [0.82579068, 0.91512478, 0.06833034]],
              [[0.05440634, 0.65857693, 0.30296619],
               [0.06769833, 0.96031863, 0.51293743]],
              [[0.09143215, 0.71893382, 0.45850679],
               [0.58256464, 0.59005654, 0.56266457]],
              [[0.71600294, 0.87392666, 0.11434044],
               [0.8694668, 0.65669313, 0.10708681]],
              [[0.07529684, 0.46470767, 0.47984544],
               [0.65368638, 0.14901286, 0.23760688]]])

a = np.hstack(b)
print(a)
# Ejercicio 5.1

for e in b:
    for e2 in e:
        if e2[2]<= 0.5:
            print("Estos son los numeros iguales o menores a", "=", e2[2])

lst = [e2[2] for e in b for e2 in e if e2[2] <=.5]
print("Estos son los numeros iguales o menores a", "=",lst)

# Ejercicio 6

import os
files = []
for f in os.listdir("../data/"):
    if f.endswith('csv'):
        files.append(f)
print (files)

lst = [f for f in os.listdir("../data") if f.endswith('csv')]
print(lst)

# Ejercicio 7
import pandas as pd

data = [pd.read_csv(os.path.join("../data", f)) for f in lst]
print(data)

data1 = pd.concat(data, axis=0)
print(data1.head(10))

# Ejercicio 8

c = [g for g in data1._get_numeric_data() if data1[g].mean()<0.48]
print(c)

# Ejercicio 9

data2 = pd.DataFrame(data1)
data2[20] = [m-1 for m in data2 ['19']]
print(data2)
# Ejercicio 10

for e in data1.values:
    for e1 in e:
        if e1 < 0.75 and e1 > 0.7:
            print(e1)
lsst = [e1 for e in data1.values for e1 in e if e1 < 0.75 and e1 > 0.7]
print(lsst)
