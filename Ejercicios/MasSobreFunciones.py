def ProcesoInicial():
    print('Buscar una hoja de papel')

def ProcesoDos():
    print('Doblar la hoja')

def SaludarATodos(*nombres):  #no se la cantidad de parametros necesito
    for i in nombres:
        print(f'hola:{i}')

def SaludarATodosDict(**nombres):
    for i in nombres:
        print(f'hola:{i} {nombres[i]}')

def Ciudades(Pais,ciudad='Oslo'):
    print(Pais,'',ciudad)

ProcesoInicial()
ProcesoDos()
colores=['azul','rojo','amarillo']
SaludarATodos('Olga')
SaludarATodos('Rafaela','Carla','Pedro')
SaludarATodos('Diego','Cynthia','Alvaro','Emiliano')
SaludarATodos()  
SaludarATodos(345,'Miryan',True) 
SaludarATodos(colores,'Helga') 

SaludarATodosDict(nombre="Vanessa",apellido="Machordom")

Ciudades('Colombia','Bogota')
Ciudades('Mexico','Ciudad de Mexico')
Ciudades('Noruega')