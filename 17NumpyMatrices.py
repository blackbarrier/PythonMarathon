import numpy as np

#Esto es para limpiar la consola.
import os
def limpiar():
    os.system("cls")

A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

print(A[0,0])

#Todo de la columna 0.
print(A[:,0])

print(A[:,1])

#Todo de la fila 1.
print(A[1,:])

#Forma de matriz
print(A.shape)

#-----------------------------------------------
#Slicing matriz. Acordate que el ultimo numero (Indice STOP) limita pero no incluye.
#
#           ROW         COLUMN
#       A[START:STOP , START:STOP]
#
print(A[1:2 , 0:2])
print(A[1:2 , :2])
print(A[:2 , 0:2])

#Ejercicio imprimir 5 y 8.
print(A[1:,1:2])

#---------------------Matriz aleatoria.
limpiar()

#Doble parentesis porque el parametro es una tupla.
A = np.random.random((2,2))
print(A)

#Hay una manera de GENERAR MATRICES ALEATORIAS DE EN UN RANGO DE NUMEROS DETERMINADO
#Me parece por el momento inncesario. Adjunto link.
#https://www.youtube.com/watch?v=PYfcybsw9LM&t=9894s&ab_channel=PythonMarat%C3%B3n




#---------------------Matriz de ceros. np.zero()  VS. np.zeros_like()-------
limpiar()
A = np.random.random((2,4))
print(A)

B = np.zeros_like(A)
print(B)

C = np.zeros((3,3))
print(C)

#Basicamente son matrices de 0. zeros_like, copia el rango de otra matriz
#y la completa con 0. zeros() crea una matriz de rango determinado.

#---------------------------------Sum
limpiar()

A=np.array([[-2,2,1,2],
            [0,1,-2,2],
            [1,1,0,0],
            [2,0,-1,0]])

print(A)

print(sum(A),"Nos da como resultado la suma de cada COLUMNA")
print(np.sum(A),"Nos da la suma todos los ELEMENTOS")
print(np.sum(A,axis=0),"Nos da como resultado la suma de cada COLUMNA(Si, igual que sum)")
print(np.sum(A,axis=1),"Nos da como resultado la suma de cada FILA.")



