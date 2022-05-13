#Zonas horarias
from datetime import datetime
from pytz import timezone
import pytz
#print(pytz.all_timezones) #todas las zonas horarias que existen
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))