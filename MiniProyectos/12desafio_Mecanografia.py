

# Crea una funcion de prueba mecanográfica.
# Toma una oracion con palabras unicas como una cadena.
# Se le pedira al ususario que esriba lo mas rapido y con la 
# mayor precicion posible.
# Se evaluara velocidad y PALABRAS acertadas.

import time

porcentaje=0

def palabrasCorrectas(f,fu):
    f=set(f.split(" "))
    fu=set(fu.split(" "))
    interseccion=f.intersection(fu)
    # interseccion=f & fu   ///Es igual
    total=len(f)
    correctas=len(interseccion)
    relacion=str(correctas)+"/"+str(total)
    porcentaje=correctas*100/total
    resultado= "Palabras acertadas: "+str(relacion)+". Un porcentaje de "+str(porcentaje)
    return print(resultado)


def main(frase):
    print("Bienvenido a la prueba mecanográfica")
    print("Debera escribir la siguinte frase. Se le tomara el tiempo.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print('"',frase,'"')
    time.sleep(1.25)
    input("Presione ENTER para comenzar.")
    print("Iniciando prueba en 3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)
    print("Ya!")

    inicio=time.time()
    fraseUsuario=input()
    fin=time.time()

    tiempo=fin-inicio
    print("Excelente! Su resultado esta siendo evaluado")
    time.sleep(1.5)

    print("Su timpo fue de ",tiempo)
    palabrasCorrectas(frase,fraseUsuario)
    
        

main("Pablito clavo un clavito")