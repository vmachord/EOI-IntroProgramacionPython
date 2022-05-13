ciudad="madrid"
print(ciudad.isdigit())
minombre="vanessa"
print(len(minombre))

print(minombre[0])
print(minombre[1])
print(minombre[4])
#print(minombre[7]) Error out of index
print(minombre[2:])
print(minombre[:3])
print(minombre[2:4])
print(minombre[-2]) #me muestra posicion 2 de la cadena
print(minombre[1:10]) #me muestra hasta el carcater q exista
print(minombre[-4])

mensaje = "dd"
print("hola {}".format(mensaje))
print("hola "+mensaje)

ciudad = "albacete"
print("hola {m} de {c}".format(m=mensaje,c=ciudad))
#print ("hola "+mensaje) No es una forma eficiente de concatener cadenas de caracteres

numero = 10/3
print("El numero sin formato es:{}".format(numero))

print("El numero con formato es:{n:1.2f}".format(n=numero))

print(f"Hola {mensaje} de {ciudad}")