# Generar un archivo CSV con los datos de status.txt que nos indica si las rutas estan abiertas o cerradas
# El formato del archivo CSV es:
# status, valenciana, borja
# todas las rutas estan abiertas, 1, 1
# todas las rutas estan cerradas, 0, 0
# la ruta de valenciana esta abierta, 1, 0
# la ruta de borja esta abierta, 0, 1

def eliminar_duplicados():
    status_unicos = set()

    with open ('status.txt', 'r') as f:
        for line in f.readline():
            status_unicos.add(line.strip())

    print(len(status_unicos))

def limpiar_datos(statuses)
    # stetuses es una lista de strings que representan los estados de los trails
    status_limpio = []
    for status in statuses
        lineas = status.replace(',' , ' ')
        lineas = status.replace('?' , '')
        lineas = status.replace('!' , '')
        lineas = status.replace('.' , ' ')
        status_limpio.append(lineas) 
    return status_limpio
