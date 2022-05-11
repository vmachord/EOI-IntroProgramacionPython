#no se puede modificar elementos, es finto
dias=('Lun','Mar','Mie','Jue','Vie','Sab','Dom') #tupla
#listas puedo poner, sacar elementos etc
dias2=['Lun','Mar','Mie','Jue','Vie','Sab','Dom'] #lista

for dia in dias:
    print(dia)

#enumerate(dias,1) enumero tupla a partir de 1
for dia_numero in enumerate(dias,1):
    print(dia_numero)

letras='abcdefghijklmnopqrstuvxyz'

letrasDelAlfabeto=tuple(x for x in letras)
#'abcdefghijklmnopqrstuvxyz' cadena que va ser ecorrida

for letra in letrasDelAlfabeto:
    print("letra:",letra)

#lo anterior es lo mismo que hacer:
for letra in letras:
    print("letra:",letra)

for letra in enumerate(letrasDelAlfabeto,40):
    print("letra:",letra)

#Desempaquetar los valores de la tupla
postres=('tiramisu','flan','pudin')
#unpakin
postrea,postreb,postrec=postres                #Unpacking elemnetos en la tupla asignados a
                                               #variables.
nuevospostres=(postrea,postreb,postrec)        #Packing de tuplas (Variables asignadas a listas)

print("Postres en la nueva tupla, R=YES:",nuevospostres)
print("Postres en la tupla:",postres)
print("Valores Unpacking",postrea,postreb,postrec)