import numpy as np 
import time
from sympy import init_printing, Matrix
import os
init_printing()


def evaluar_ganador(A,dimension,ganador): 
     
    #Fila
    for x in range(0,dimension[1]-1):
        fila=A[x,:]
        lista_fila=list(fila)
        for i in range(len(lista_fila) - 3):
            if all(lista_fila[i:i+4]):
                ganador=True


    #Columna
    for x in range(0,dimension[0]-1):
        col=A[:,x]
        lista_col=list(col)
        for i in range(len(lista_col) - 3):
            if all(lista_col[i:i+4]):
                ganador=True

    return ganador


def modificar_matriz(A, seleccion,jugador, dimension):
        A[fondo,seleccion]=jugador
        #Modificar la matriz
        


def verificar2(seleccion, dimension):
    #La seleccion ya ingresa indexada a esta funcion.
        fondo=-1
        while A[fondo,seleccion]!=0 and (fondo*-1)-1<=dimension[0]:
            fondo-=1
        if fondo<=dimension[0]:            
            return True
        else:
            print("Columna llena")
            

def verificar(seleccion, dimension):
    if seleccion.isdigit():
        seleccion=int(seleccion)
        seleccion-=1        
        if seleccion >=0 and seleccion<dimension[1]:
            verificar2(seleccion, dimension)
            return seleccion        
    return None



def turnos(A,dimension):
    print(A)
    print("Comienza jugador 1")
    seleccion=input("Ingrese numero de columna")
    seleccion=verificar(seleccion, dimension)
    while seleccion()==None:
        print("Seleccion incorrecta. Intente de nuevo.")
        seleccion=input("Ingrese numero de columna")
        seleccion=verificar(seleccion, dimension)
    modificar_matriz(A,seleccion)




def main():
    dimension=(6,7)
    A = np.zeros(dimension)

    print("Bienvenido a 4 en linea")
    print("Jugara con otro jugador en esta oportunidad")
    print("Comienza...")

    turnos(A,dimension)    

    print("Juego finalizado!")


main()
