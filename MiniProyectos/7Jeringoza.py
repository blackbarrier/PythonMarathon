#Traductor de jeringoza
#Agregar runa p despues de cada vocal
#Repetir la vocal

palabra=input("Ingresa una palabra: ")
traduccion=""

for letra in palabra:
    if letra in "aeiouAEIOU":
        letra+="p"+letra
    traduccion+=letra

print("Traduccion: ",traduccion)