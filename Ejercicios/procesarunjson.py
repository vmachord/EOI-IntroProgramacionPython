import json
# jsonventas = json.loads(" ORIGIN DE LOS DATOS DEL JSON")
jsonventas='{"departamentos": 8,"nombredepto": "Ventras","director": "Juan Rodriguez","empleados": [{"nombre": "Pedro","apellido": "Fernandez"},{"nombre": "Jacinto","apellido": "Benavente"}]}'
#segundoJson="{'departamentos': 8,'nombredepto': 'Ventras','director': 'Juan Rodriguez','empleados': [{'nombre': 'Pedro','apellido': 'Fernandez'},{'nombre': 'Jacinto','apellido': 'Benavente'}]}"
#tercerJson= "{\"departamentos\": 8,\"nombredepto\": \"Ventras\",\"director\": \"Juan Rodriguez\",\"empleados\": [{\"nombre\": \"Pedro\",\"apellido\": \"Fernandez\"},{\"nombre\": \"Jacinto\",\"apellido\": \"Benavente\"}]}"

# ' inicia y finaliza contenido de variable
print(jsonventas)
print(type(jsonventas))

datosDepartamento=json.dumps(jsonventas) #Serializacion de un Objeto a JSON (JSON es un string)
print(type(datosDepartamento))

jsonventas = json.loads(jsonventas) #Deserializacion de un JSON a Objeto
print(type(jsonventas))
#datosSegundoDepto = json.dumps(segundoJson)
#datosTercerDepto = json.dumps(tercerJson)

print("Json 1",datosDepartamento)
#print("Json 2",datosSegundoDepto)
#print("Json 2",datosTercerDepto)

print(type(datosDepartamento))
# Conclusion:
# la variable que debo utilizar para procesar el JSON como una coleccion compleja (compuesta) es el deserializado (loads)
for val in jsonventas:
    print(val)
#
for val in jsonventas:
    if(val!='empleados'):
        print(val,":",jsonventas[val])
    else:
        print('Integrantes del departamento:')
        for integrantes in jsonventas['empleados']:
            print('\t\t',integrantes['nombre'],' ',integrantes['apellido'])