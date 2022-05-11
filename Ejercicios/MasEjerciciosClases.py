#-------Ejercicio 1-------

# class Jets:
#    def __init__(self, name, country):
#        self.name = name
#        self.origin = country
        
#first_item = Jets("F16", "USA")
#Escriba su respuesta aquí.
#a=first_item.name
#print(a)

#-------Ejercicio 2-------

#class Jets:
#    model = None
#    country = 0

#    def __init__(self, name, country):
#        self.name = name
#        self.origin = country

#first_item = Jets("F16", "USA")
#Escriba su respuesta aquí.
#b=first_item.origin
#print(b)

#-------Ejercicio 3-------

#class Jets:
#    model = None
#    country = 0
#    def __str__(self):
#        return "{}->{}".format(self.name, self.origin)

#    def __init__(self, name, country):
#        self.name = name
#       self.origin = country
#Escriba su respuesta aquí.   
      
#first_item=Jets("F14","USA")
#second_item=Jets("SU33","Russia")
#third_item=Jets("AJS37","Sweden")
#fourth_item=Jets("Mirage2000","France")
#fifth_item=Jets("Mig29","USSR")
#sixth_item=Jets("A10","USA")
###first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]
###first_army=[first_item,second_item,third_item,fourth_item,fifth_item,sixth_item] #uso objeto para crear lista, no me considera como cadena de caracteres si como objetos
#first_army=["avion:{}".format(first_item),str(second_item),str(third_item),str(fourth_item),str(fifth_item),str(sixth_item)]
#print(first_army)

#-------Ejercicio 4-------

#class Jets:
#    model = None
#    country = 0
#    def __init__(self, name, country,cantidad):
#        self.name = name
#        self.origin = country
#        self.quantity = cantidad
#Escriba su respuesta aquí. 
     
#first_item=Jets("F14","USA",87)
#second_item=Jets("Mirage2000","France",35)
#total=first_item.quantity + second_item.quantity
#print(total)

#-------Ejercicio 5+6-------

#Escriba su respuesta aquí.
class Nobel:
    def __init__(self, categoria, anio,ganador):
        self.category = categoria
        self.year = anio
        self.winner = ganador
    def __str__(self):
        return "{} ({}): {}".format(self.winner, self.year,self.category)

nq2019=Nobel("Chemistry", 2019, "John B. Goodenough")
#print(nq2019.category, nq2019.year, nq2019.winner)
print(nq2019)

#-------Ejercicio 7-------
#class myfunc: 
#    def quinta(x):
#        return pow(x,5)

#ans=myfunc.quinta(5)
#print(ans)

#-------Ejercicio 8-------

class myfunc: 
    def ElevarAlaPotencia(x,y):
        return pow(x,y)
    def __str__(self):
        return "Esta clase consistirá en operaciones matemáticas. Solo tenemos una función llamada ElevarAlaPotencia."

ans1 = myfunc.ElevarAlaPotencia(5, 6)
ans2 = myfunc()

print(ans1)
print(ans2)



















