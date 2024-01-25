#Conjuntos
#Es recomendable usarlos en lugar de las listas 
#(cuando sea viable). En teoria es mas repido(?. Invesigar.

#Definicion
In [40]: x={1,2,2,3,4,4,5}

In [41]: x
Out[41]: {1, 2, 3, 4, 5}

#Crear conjunto vacio
In [42]: x=set()

In [43]: x
Out[43]: set()

#Adicionar

In [44]: x.add(3)

In [45]: x.add("stres")

In [46]: x
Out[46]: {3, 'stres'}

#Discard y Remove
#Discard elimina elementos y remove elimina SOLO si
#existen en el conjunto. Si no existe en el conjunto
#arroja un error.   
In [47]: x.remove(3)

In [48]: x
Out[48]: {'stres'}

In [49]: r.remove(11)
# ----> 1 r.remove(11)
# NameError: name 'r' is not defined

#---------------------------------------------------------

In [26]: "dictionaries"
Out[26]: 'dictionaries'

#Se define clave valor.
In [27]: x={"one":1,2:"two","three":[1,2,3]}

In [28]: x
Out[28]: {'one': 1, 2: 'two', 'three': [1, 2, 3]}

In [29]: type(x)
Out[29]: dict

#Se accede al velor mediante la KEY
In [30]: x[2]
Out[30]: 'two'

#Vaciamos diccionario
In [33]: x={}

#Definicion de clave/valor. Se hace como una llamada mediante
#la clave. Y se le asigna un valor inmediatamente.

In [34]: x[1]="uno"

In [35]: x[1]
Out[35]: 'uno'

In [36]: x
Out[36]: {1: 'uno'}


#Ver todas las claves

In [37]: x.keys()
Out[37]: dict_keys([1])

#Ver todos los valores

In [38]: x.values()
Out[38]: dict_values(['uno'])