import numpy as np 
import time
from sympy import init_printing, Matrix
import os
init_printing()


def limpiar():
    os.system("cls")

def imprimir_titulo():
    print("$$\   $$\                                 $$\ $$\                               ")
    print("$$ |  $$ |                                $$ |\__|                              ")
    print("$$ |  $$ |       $$$$$$\  $$$$$$$\        $$ |$$\ $$$$$$$\   $$$$$$\   $$$$$$\  ")
    print("$$$$$$$$ |      $$  __$$\ $$  __$$\       $$ |$$ |$$  __$$\ $$  __$$\  \____$$\ ")
    print("\_____$$ |      $$$$$$$$ |$$ |  $$ |      $$ |$$ |$$ |  $$ |$$$$$$$$ | $$$$$$$ |")
    print("      $$ |      $$   ____|$$ |  $$ |      $$ |$$ |$$ |  $$ |$$   ____|$$  __$$ |")
    print("      $$ |      \$$$$$$$\ $$ |  $$ |      $$ |$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |")
    print("      \__|       \_______|\__|  \__|      \__|\__|\__|  \__| \_______| \_______|")
    print()
    print()


def bievenida(A):
        print("Bienvenido a '4 en linea'")
        print("Un emocionante juego para 2 jugadores.")
        print("Este es su tablero:")
        print()
        print(A)
        print()
        input("Pulse cualquier tecla para comenzar...")

def verificar(seleccion,A):
    #Verifica que la seleccion sea un digito y este dentro del rango.
    if seleccion.isdigit():
        seleccion=int(seleccion)
        seleccion-=1        
        if seleccion >=0 and seleccion<A.shape[1]:
            return seleccion 
    print("Seleccion incorrecta. Ingrese numero de columna.")   
    return None


def verificar2(seleccion, A):
    #La seleccion ya ingresa indexada a esta funcion. Verifica que la columna no este llena.
        columna=A[:,seleccion]    
        for elemento in columna:
            if elemento==0:
                return seleccion
            else:
                print("Columna llena. Elija otra.")
                return None
                

def modificar_matriz(A, seleccion, jugador):
    fondo=-1
    while A[fondo,seleccion]!=0:
        fondo-=1
    A[fondo,seleccion]=jugador
    return A
    
            
def evaluar_ganador(A):
    dimension=A.shape

    #Fila
    for i in range(0,dimension[0]):
        fila=(A[i,:])
        for i in range(len(fila)-3):
            if fila[i]!=0:
                if fila[i]==fila[i+1] and fila[i+1]==fila[i+2] and fila[i+2]==fila[i+3]:
                    return True
    #Columna
    for i in range(0,dimension[1]):
        col=(A[:,i])
        for i in range(len(col)-3):
            if col[i]!=0:
                if col[i]==col[i+1] and col[i+1]==col[i+2] and col[i+2]==col[i+3]:                    
                    return True
    return False


def turnos(A):
    jugador=1
    juegoFinalizado=False
    
    while juegoFinalizado==False:        
        seleccion=None
        while seleccion==None:
            limpiar()            
            imprimir_titulo()
            
            print(A)
            print()
            print("Turno: Jugador",jugador)
            print("Ingrese numero de columna:")
            print()
            seleccion=input()
            seleccion=verificar(seleccion, A)            
            if seleccion!= None:
                seleccion=verificar2(seleccion, A)   

        A=modificar_matriz(A,seleccion,jugador) #Esta funcion recibe una seleccion completamente VALIDA dentro del rango y en columna NO llena.
        if evaluar_ganador(A)==True:
            juegoFinalizado=True
            return jugador
        else:
            if jugador==1:
                jugador=2
            else:
                jugador=1


def main():
    dimension=(6,7)
    A = np.zeros(dimension)
    limpiar()
    imprimir_titulo()
    bievenida(A)
    ganador=turnos(A)
    limpiar()
    print("Juego finalizado!")
    print(A)
    print()
    print("Ganador: Jugador",ganador)


main()
