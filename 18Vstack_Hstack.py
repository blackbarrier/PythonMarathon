import numpy as np
#Esto es para limpiar la consola.
import os
def limpiar():
    os.system("cls")

x = np.array([[1,2,3],[0,0,1],[1,1,3]])

y = np.array([[1,0,-1],[4,0,1],[1,-1,0]])

# print(x)
# print(y)

print(np.vstack((x,y)))
#VerticalStack.... condicion excluyente: Igual cant. de COLUMNAS.






#------------HStack
limpiar()

x = np.array([[1,12,2],[3,-1,2],[1,2,0]])
y = np.array([[0,-2,2],[0,-1,4],[1,0,0]])

print(x)
print(y)

print("//////////")
#HorizontalStack.... condicion excluyente: Igual cant. de FILAS.
print(np.hstack((x,y)))

#-----------Existe "Split" para dividir matrices en partes iguales.

#-----Mascara

In [3]: A = np.array([[1,2,3],[4,5,6],[7,8,9]])

In [4]: A
Out[4]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

In [5]: mascara = A > 5

In [6]: mascara
Out[6]:
array([[False, False, False],
       [False, False,  True],
       [ True,  True,  True]])

In [7]: A[mascara]
Out[7]: array([6, 7, 8, 9])

In [8]: A
Out[8]:
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])