#Traductor de jeringoza
#Agregar runa p despues de cada vocal
#Repetir la vocal

L=["perro","gato","canario","elefante","lobo","delfin"]

def traducir(L):
    string=""

    for palabra in L:

        palabraTraducida=""

        for letra in palabra:
            if letra in "aeiouAEIOU":
                letra=letra+"p"+letra
            palabraTraducida+=letra

        if palabra==L[0]:
            palabraTraducida=palabraTraducida.capitalize()
            palabraTraducida+=", "
        elif palabra==L[-1]:
            palabraTraducida+="."
        else:
            palabraTraducida+=", "
            
        string+=palabraTraducida        

    print(string)



traducir(L)