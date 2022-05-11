Op = input("Ingrese operación: ")

try:

    if('+' in Op):

        Op = Op.split('+')
        print(f"El resultado es {float(Op[0]) + float(Op[1])}")

    elif('-' in Op):

        Op = Op.split('-')
        print(f"El resultado es {float(Op[0]) - float(Op[1])}")

    elif('/' in Op):

        Op = Op.split('/')
        print(f"El resultado es {float(Op[0]) / float(Op[1])}")

    elif('*' in Op):

        Op = Op.split('*')

        try:

            print(f"El resultado es {float(Op[0]) * float(Op[1])}")

        except ZeroDivisionError:

            print("Error, división entre 0")

except ValueError:

    print("Por favor, escriba un valor numérico válido")