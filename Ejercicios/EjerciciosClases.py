class Persona:
    Nombres=""
    Apellidos=""
    
    def __init__(self,nombres,apellidos):
        self.Nombres = nombres
        self.Apellidos = apellidos

    def caminar(self):
        print('caminando')

    def __str__(self):
        return "{} {}".format(self.Nombres,self.Apellidos)

#class a:
#    def tobyte():
#        pass

profesor = Persona("Vanessa","Machordom") #creo objeto con constructor por defecto
#profesor.Nombres="Vanessa"      #setter
#profesor.Apellidos="Machordom"  #setter

alumno = Persona("Pedro","Sanchez") #uso mi constructor nuevo
#alumno.Nombres="Pedro"
#alumno.Apellidos="Sanchez"

administrativo = Persona("Oscar","Leon")
#administrativo.Nombres="Oscar"
#administrativo.Apellidos="Leon"

#a=1 --> tipo int
#print(type(a))
print("El profesor: {} {}".format(profesor.Nombres,profesor.Apellidos)) #getter
print("El alumno: {} {}".format(alumno.Nombres,alumno.Apellidos))
print("El administrativo: {} {}".format(administrativo.Nombres,administrativo.Apellidos))

print("El Alumno :",alumno)
profesor.caminar()