import numpy as np
import time

def piedra_papel_tijera():

    #Definicion de jerarquias
    opciones={"piedra":"tijera","tijera":"papel","papel":"piedra"}
    
    #Entrada de jugador
    jugador= input("Ingrese piedra, papel o tijera: ")
    while jugador not in {"piedra", "papel", "tijera"}:
            print("Cometiste un error")
            jugador= input("Ingrese piedra, papel o tijera: ")
    
    #Entrada de computadora
    computadora=np.random.choice(["piedra","papel", "tijera"])

    #Mensaje
    time.sleep(.5)
    print("Has seleccionado ",jugador)
    print("La computadora ha seleccionado ",computadora)

    time.sleep(2)

    #Evaluar ganador
    if opciones[jugador]==computadora:
          print("Has ganado")
    elif opciones[computadora]==jugador:
          print("Has perdido")
    else:
          print("Has empatado")

piedra_papel_tijera()