#Asignacion simultanea
a=5
b=10
print("Paso 1.Valores Iniciales")
print(a)
print(b)
c=b
b=a #perdemos el valor de b, pasa a valer a
a=c
del c
print("Paso 2. Valores Intercambiados")
print(a)
print(b)
