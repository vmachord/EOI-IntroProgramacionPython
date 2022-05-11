#Area y Volumen de un cilindro
import math
Rd=input("Introduce el Radio: ") #Base
Ho=input("Introduce el Ho: ")   #Altura
if(Rd.isdigit() and Ho.isdigit()):
    Rd=int(Rd)
    Ho=int(Ho)
    pi=math.pi #3.1415
    print('El Area del cilindro es: {n:1.2f} y El Volumen: {m:1.2f}'.format(n=(pi*2)*Rd*Ho+(pi*2)*(Rd*Rd),m=pi*(Rd*Rd)*Ho))
else:
    print("Introduce un numero valido")


