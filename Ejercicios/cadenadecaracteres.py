ubicacion="Madrid capital de España"
print(ubicacion.upper())
print(ubicacion.lower())
aes="cawaaaaaaaa"
nueva = aes.replace('a','b')
print(nueva)
nueva = aes.replace('a','b',4)
print(nueva)
print(ubicacion.split(' '))
ubicacion = '\t\t Madrid capital de España'
print(ubicacion.strip())
print(ubicacion.count('a'))
print(ubicacion.strip().endswith('paña'))
print(ubicacion.strip().upper().startswith('MADRID'))
datos="Pais: {}, capital: {}"
print(datos.format("España","Madrid"))
pais="españa"
ciudad="madrid"
print(datos.format(pais,ciudad))