#Expliquemos funciones lambda
#Son como funciones matematicas

#Basicamente esta funcion en particular
#hace el cuadrado de x.
f = lambda x: x**2

#Cuando la llamo reemplazo f(x)
res=f(3)
print(res)



#Otro ejemplo

#En este caso devuelve 1 si x es >=10 sino -1
f= lambda x: 1 if x >=10 else -1
print(f(11))