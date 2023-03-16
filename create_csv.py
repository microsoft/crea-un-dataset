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
    # statuses es una lista de strings que representan los estados de las rutas
    status_limpio = []
    for status in statuses
        lineas = status.replace(',' , ' ')
        lineas = status.replace('?' , '')
        lineas = status.replace('!' , '')
        lineas = status.replace('.' , ' ')
        status_limpio.append(lineas) 
    return status_limpio

def normalizar_datos(statuses)
    status_normalizados = []
    for status in statuses:
        status_normalizados.append(status.lower())
    return status_normalizados

def identificar_status(statuses):
    # status, valenciana, borja
    # regresar status, 0, 0
    # status, 1, 1
    valores = []
    for status in statuses:
        if "todas las rutas estan abiertas" in status:
            valores.append([status 1, 1,])
        elif "yodas las rutas estan cerradas" in status:
            valores.append([status, 0, 0])
        elif "ruta esta abiertas" in status:
            valores.append([status, 1, 1])
        elif "ruta esta cerradas" in status:
            valores.append([status, 0, 0])    
        elif "valenciana esta cerrada" in status and "Borja esta cerrada" in status:
            valores.append([status, 0, 0])
        elif "valenciana esta cerrada" in status and "Borja esta abierta" in status:
            valores.append([status, 0, 1])
        elif "valenciana esta abierta" in status and "Borja esta cerrada" in status:
            valores.append([status, 1, 0])
    return valores

def main():
    status = eliminar_duplicados()
    status = limpiar_datos(status)
    status= normalizar_datos(status)

    with open ('status.csv', 'w') as f:
        import csv
        headers = ['status', 'Valenciana', 'Borja']
        writer = csv.writer(f)
        writer.writerrow(headers)
        writer.writerows(identificar_status(status))

if __name__=='__main__':
    main()
