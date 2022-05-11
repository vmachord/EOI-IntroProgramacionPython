#Ejer N1
lst1=[1,2,3,4,5]

lst2=[x for x in lst1]
print(lst2)

#Ejer N2
rng=[]
for n in range(1200,2001,130):
    rng.append(n)
#print(rng._str_)
#print(list(rng))
lst=[]
for x in rng:
    lst.append(x)
print(lst)

rng=range(1200,2001,130) #es equivalente a las lineas 9,10 y 11
lst=[x for x in rng]     #es equivalente a las lineas 14 y 15
print(lst)

#Ejer N3

lst1=[44,54,64,74,104]
lst2= []
"""
for n in lst1:
    lst2.append(n+6)
print(f"Version Larga: Lista 1: {lst1}\nLista 2: {lst2}")
"""
lista1 = [1,1,1,1,1,1,1]
lista2 = [n+6 for n in lista1]
print(f"Lista 1: {lista1}\nLista 2: {lista2}")

#Ejer N4
lst1=[2,4,6,8,10,12,14]
lst2=[(num**2) for num in lst1]

#Ejer N5
lst1=[2,4,6,8,10,12,14]
lst2=[(x**2) for x in lst1 if (x**2)>50]
print(lst2)

#Ejer N6
dict={"Susuke Ignis": 985, "Chevrolet park Activ": 1100, "Volkswagen CrossUP": 1245, "Masda CX-3": 1254, "Susuki Vitara": 1245, "Nissan Kicks": 1310, "Mazda CX-5": 1672, "Ford Escape": 1625}

lst=[x.upper() for x in dict if dict[x]<1300]
print(lst)

#Ejer N7
lst=["NY", "FL", "CA", "VT"]
dict={x:x for x in lst}
print(dict)

#Ejer N8
rng=range(100,161,10)
dict={x:x/100 for x in rng}
print(dict)

#Ejer N9
"""
Usando la comprensión de listas y un argumento 
condicional, cree un diccionario a partir del
diccionario actual donde solo los pares clave:valor
 con un valor superior a 2000 se toman en el nuevo
  diccionario.
"""

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
#Escriba su respuesta aquí.
dict2={x:dict1[x] for x in dict1 if dict1[x]>2000}

print(dict2)
