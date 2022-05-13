from datetime import datetime
import locale #cambia cultura
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')
#establezca la cultura, primero categoria, LC_TIME cambia hora, 
#la hora la quiero colocar en este formato: es_ES.UTF-8 

fechacastellano = datetime.now()

print(fechacastellano)
print("Fecha castellano:",fechacastellano.strftime("%A %d %b %Y"))