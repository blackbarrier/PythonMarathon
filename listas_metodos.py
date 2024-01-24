    
In [59]: L = [1,2,3,4,5]

In [60]: L
Out[60]: [1, 2, 3, 4, 5]

In [61]: L.append(5)

In [62]: L
Out[62]: [1, 2, 3, 4, 5, 5]

In [63]: L.pop()
Out[63]: 5

In [64]: L
Out[64]: [1, 2, 3, 4, 5]

In [65]: L.append("x")

In [66]: L.pop()
Out[66]: 'x'

In [67]: L
Out[67]: [1, 2, 3, 4, 5]

In [68]: L.extend(["a","b","c"])

In [69]: L
Out[69]: [1, 2, 3, 4, 5, 'a', 'b', 'c']

In [70]: L.pop()
Out[70]: 'c'

In [71]: L.pop()
Out[71]: 'b'

In [72]: L
Out[72]: [1, 2, 3, 4, 5, 'a']

In [73]: L.pop()
Out[73]: 'a'

In [74]: L
Out[74]: [1, 2, 3, 4, 5]

In [75]: L=[5,6,3,2,1,0,9]

In [76]: L.extend([44,32,52])

In [77]: L
Out[77]: [5, 6, 3, 2, 1, 0, 9, 44, 32, 52]

#NOTA: L.pop() solo funciona por indice, mira este ejemplo.

In [78]: L.index(44)
Out[78]: 7

#Tuve que buscar el indice para insertarlo en el pop.
In [79]: L.pop(7)
Out[79]: 44

#Combinado

In [80]: L
Out[80]: [5, 6, 3, 2, 1, 0, 9, 32, 52]

In [81]: L.pop(L.index(32))
Out[81]: 32



In [82]: L
Out[82]: [5, 6, 3, 2, 1, 0, 9, 52]

In [83]: L.pop()
Out[83]: 52

In [84]: L.append("x")

In [85]: L
Out[85]: [5, 6, 3, 2, 1, 0, 9, 'x']

In [86]: L.extend([33,"y",12])

In [87]: L
Out[87]: [5, 6, 3, 2, 1, 0, 9, 'x', 33, 'y', 12]


#En vez de combinar pop() con index() podemos usar remove para buscar por valor. Elimina solo el primer valor.
#Podemos ver que remove() elimina el primer 
In [88]: L.remove("x")
In [89]: L
Out[89]: [5, 6, 3, 2, 1, 0, 9, 33, 'y', 12]

In [90]: L.append("y")
In [91]: L
Out[91]: [5, 6, 3, 2, 1, 0, 9, 33, 'y', 12, 'y']

In [92]: L.remove("y")
In [93]: L
Out[93]: [5, 6, 3, 2, 1, 0, 9, 33, 12, 'y']

#Ordenamos
In [95]: L.pop()
Out[95]: 'y'
In [96]: L.sort()
In [97]: L
Out[97]: [0, 1, 2, 3, 5, 6, 9, 12, 33]

#OrdenacionInversa
In [99]: L.reverse()
In [101]: L
Out[101]: [33, 12, 9, 6, 5, 3, 2, 1, 0]

#IMPORTANTE. La ordenacion produce una nueva asignacion. Osea, la variable queda definida con un nuevo orden.

#Longitud
In [98]: len(L)
Out[98]: 9

#Contar cantidad de veces que aparece un valor
In [102]: L.count(9)
Out[102]: 1

#Inserta DELANTE del indice 0 el valor 4.
In [103]: L.insert(0,4)
In [104]: L
Out[104]: [4, 33, 12, 9, 6, 5, 3, 2, 1, 0]

#Inserta DELANTE del indice -1 el valor "final".
In [105]: L.insert(-1,"final")
In [106]: L
Out[106]: [4, 33, 12, 9, 6, 5, 3, 2, 1, 'final', 0]