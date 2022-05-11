def saludar(nombre):
    print(f'hola {nombre} buenos dias')

def sumar(a,b):
    return (a+b)

#nombre relacionado a su funcionalidad
def addColores(colores,color):
    try:
        colores.append(color)
        return True
    except AttributeError:
        return False
    

print(sumar(5,5))
saludar('Billy')
saludar('Carlos')
saludar('Helena')
saludar('Silvia')

colores=[]
addColores(colores,'azul')
addColores(colores,'rojo')
addColores(colores,'verde')
addColores(colores,'negro')
if(addColores(colores,'purpura')):
    print('Inserte el color')

saludar(colores)

if (addColores('billy','naranja')): # Equivalente addColores('billy','naranja')==True
    print('Insertado color')
else:
    print('No insertado color')

ciudad='Nairobi'