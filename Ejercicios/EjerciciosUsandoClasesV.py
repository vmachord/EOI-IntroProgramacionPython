class partner:
    def __init__(self):
        self._age = 0   #propiedad privada
    def get_age(self):
        print('getter llamado')
        return self._age
    def set_age(self,a):
        print('setter llamado')
        if (a<10):
            raise ValueError("edad no permitida")
        self._age = a
    def del_age(self):
        del self._age
    age = property(get_age,set_age,del_age)
mark = partner()
#mark.set_age(10)
#mark.age = 10 #aca property llama el set para contestar
#print(mark.age) #aca property llama el get para contestar

try:
    mark.age = 9
except ValueError:
    print("Edad no permitida")
finally:
    print(mark.age) #recupera valor del age y llama getter




