numero1 = 100
numero2 = 5
a="5"
try:
    print("otra instrucciones 1")
    print("otra instrucciones 2")
    print("otra instrucciones 3")
    print("otra instrucciones 4")
    print(numero1/numero2)
    print("otra instrucciones 5")
    c=int(a)
    print("otra instrucciones 6")
    print("otra instrucciones 7")
except ZeroDivisionError:
    print("Error, al dividir por cero")
except ValueError:
    print("Error, Valor a convertir a numero desde texto erroneo")
except: #esto vale para cualquier otro error
    print ('Error')
else:
    print("Las instrucciones se completaron en su totalidad")
finally:
    print('fin del programa')