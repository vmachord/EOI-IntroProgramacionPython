def Fibonacci(N):
    if N < 2:
        return N
    else: 
        return Fibonacci(N-1)+Fibonacci(N-2)

N=input("Que numero de la serie de Fibonacci quiere?")
try:
    N=int(N)
    if (N>0):
        numeroDeLaSerie = N-1
        actual=Fibonacci(numeroDeLaSerie)
        print(actual)
    else:
        print("Debe entrar un numero mayor que 0")
except ValueError:
    print("Entrada invalida")