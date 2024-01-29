
from matplotlib import pyplot as plt 
import numpy as np

#Declaracion de funcion
f= lambda x:np.sin(x)

#Configuro propidades de plt para los titulos. Pyplot permite hacer graficos.
plt.title("Sen (x)")
plt.xlabel("Eje x")
plt.ylabel("Eje y")

#En esta instancia vamos a pedir que grafique.
#Lo que hariamos a mano es darle los valores de X uno a uno y veriamos su correspondiete Y.
#Python nos permite darle muchos numeros a la vez (Linspace)

#(punto de partida, punto final, cantidad de puntos en total entre extremos)

x = np.linspace(-10, 10, 100)

#Trazo la funcion (valor X, valor Y, otroParametro)
plt.plot(x,f(x), "mD")

#El string "md" indica "magenta" y fomrma de "diamante".
#Hay muchas propiedades. Podes investigar.

#Muestro
plt.show()