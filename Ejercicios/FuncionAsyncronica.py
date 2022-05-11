#FuncionAsyncronica.py

import asyncio

async def saludo():
    print('Hola')
    await asyncio.sleep(4) #duerme el programa, espera 4 segundos
    print('... mundo')

asyncio.run(saludo())
print('Fin del programa')