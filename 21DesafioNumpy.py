import numpy as np

A  = np.load("##num.npy")
final=A.shape[0]


coleccion=[]
mayor_prod=0

for i in range(final-13):
    seleccion=(A[i:i+13])
    prod_seleccion=1
    for j in seleccion:
        prod_seleccion=j*prod_seleccion

   
    if prod_seleccion>mayor_prod:
        mayor_prod=prod_seleccion

print(mayor_prod)