import numpy as np 

A=np.random.random((5,5))
print("La matriz creada es:")
print(A)

np.save("ejemplo.npy",A)
#Lo guarda en el directorio actual


#_------Cargar
#Inicialiamos A para que quede vacio y asi verificar que estoy cargando bien.
A="Se ha borrado la variable A"
print(A)

print("La matriz CARGADA es:")
A  = np.load("ejemplo.npy")
print(A)

print("Vemos que se cargo la misma matriz de manera correcta")