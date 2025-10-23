import csv
#crear la lista de temperatura, humedad y precion y leer los datos del archivo
humedad = []
with open('C:\\Users\\jesus david\\Documents\\variable.csv', 'r') as csvfile:
        lector = csv.reader(csvfile, delimiter=';')  #se utiliza el metodo reader
        encabezado = next(lector)
        for fila in lector:            #con el for se itera sobre el objeto paara leer
            dato = fila[2]     #0,84
            dato = float(dato.replace(',', '.'))  #0.84
            humedad.append(dato)

print(encabezado[2])
print(humedad)
        