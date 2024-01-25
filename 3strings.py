
# Declaracion variable
In [12]: cadena="cadena"

In [14]: cadena
Out[14]: 'cadena'

#Busqueda por indice
In [15]: cadena[1]
Out[15]: 'a'

#Busquda por rango
In [16]: cadena[1:4]
Out[16]: 'ade'

#Busqueda por indice inverso
In [17]: cadena[-1]
Out[17]: 'a'

#Busqueda por indice "intermitente"
In [18]: cadena[::2]
Out[18]: 'cdn'

#Inversion de caracteres
In [19]: cadena[::-1]
Out[19]: 'anedac'

#Busqueda por indice "intermitente" inversa
In [20]: cadena[::-2]
Out[20]: 'aea'

#Rango del [1 al 5], saltos cada [3].
In [21]: cadena[1:5:3]
Out[21]: 'an'

#Comienza a contar desde la ultima "a", cuenta 3 desde el final sin incluir el 3 (sin incluir la "e"). El -1 Indica que sera en orden inverso sin saltos.
In [22]: cadena[-1:3:-1]
Out[22]: 'an'

#Mayusculas
In [24]: cadena.upper()
Out[24]: 'CADENA'

#Minusculas
In [25]: cadena.lower()
Out[25]: 'cadena'

#Minusculas??
In [28]: cadena.islower()
Out[28]: True

#Mayusculas?
In [29]: cadena.isupper()
Out[29]: False

#Invertir Mayusculas
In [30]: cadena.swapcase()
Out[30]: 'CADENA'

In [31]: "ffFFffR".swapcase()
Out[31]: 'FFffFFr'

#Reemplazo de caracteres
In [33]: cadena.replace("a","b")
Out[33]: 'cbdenb'

In [34]: cadena.replace("cad","queso")
Out[34]: 'quesoena'

#Contar cantidad de caracter
In [35]: cadena.count("a")
Out[35]: 2

In [36]: cadena.count("D")
Out[36]: 0

In [37]: cadena.count("d")
Out[37]: 1

#Es alfanumerico? Decimal? Digito?(Numerico)

In [38]: cadena.isalpha()
Out[38]: True

In [39]: cadena.isdecimal()
Out[39]: False

In [40]: cadena.isdigit()
Out[40]: False

In [41]: "123".isalpha()
Out[41]: False

In [42]: "123".isdecimal()
Out[42]: True

In [43]: "123".isdigit()
Out[43]: True

#Contar indice de caracter. El primer caracter encontrado en el string.
In [44]: cadena.index("a")
Out[44]: 1

#Particion de string por caracter (Lo incluye)
In [45]: cadena.partition("d")
Out[45]: ('ca', 'd', 'ena')

#Particion de string por caracter (No lo incluye)
In [46]: cadena.split("d")
Out[46]: ['ca', 'ena']