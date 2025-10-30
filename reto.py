import os
import csv
import matplotlib.pyplot as plt

def contar_palabras_y_caracteres(ruta):
    if os.path.exists(ruta): #si esta ruta existe el comando "os.path" la busca y usa esa ruta para abrir el archivo
        archivo = open(ruta, "r", encoding="utf-8") #abre el archivo 
        texto = archivo.read() #lee y muestra el archivo 
        archivo.close() # cierra el archivo

        palabras = texto.split() #aca el comando "split" divide todas las palabras en una lista
        num_palabras = len(palabras) #aca se coje esa lista del paso anterior y se lee los elementos de la lista que se crea 
        num_caracteres = len(texto) #se coje el texto del archivo y se leen los caracteres 
        sin_espacios = len(texto.replace("", ""))

        print("\n--- RESULTADOS ---") #aca da el resultado para el numero de palabras dependiendo de lo que "len" encuentre 
        print("Numero de palabras:", num_palabras) #me va a arrojar el numero de caracteres 
        print("Numero de caracteres:", num_caracteres) #con espacios 
        print("Número de caracteres:", sin_espacios) #sin espacios
        categorias = ['palabras', 'caracteres', 'sin espacios']    #datos
        valores = [num_palabras, num_caracteres, sin_espacios] #grafico

        plt.bar(categorias, valores)  # Crear la gráfica de barras

        plt.title('Gráfica de Barras') # Agregar título y etiquetas
        plt.xlabel('Categorías')
        plt.ylabel('Valores')

        plt.show()  # Mostrar la gráfica 
    else:
        print("El archivo no existe en la ruta especificada.")

def reemplazar_palabra(ruta): #define la funcion de reemplazar palabras 
    if os.path.exists(ruta): #busca la ruta y si laa encuentra sigue 
        palabra = input("Palabra a reemplazar: ") # el usuario pone la palabra que desea reemplazar
        nueva = input("Nueva palabra: ") # aca se pone la palabra nueva que el usuario quiera poner 

        with open(ruta, "r", encoding="utf-8") as f: #aca se abre el archivo
            texto = f.read()

        texto_nuevo = texto.replace(palabra, nueva) #reemplazar la palabra 

        archivo = open(ruta, "w", encoding="utf-8")
        archivo.write(texto_nuevo)
        archivo.close()

        print("Palabra reemplazada correctamente.")
    else:
        print("El archivo no existe.") 






















def contar_ocurrencias(ruta):                                                #esto es la parte del grafico
    if os.path.exists(ruta):
        palabra = input("Ingrese la palabra para contar: ")
        archivo = open(ruta, "r", encoding="utf-8")
        texto = archivo.read().lower()
        archivo.close()
        lista = texto.split()
        conteo = lista.count(palabra.lower())

        print(f"La palabra '{palabra}' aparece {conteo} veces.")
    else:
        print("El archivo no se encontró.")
        



'''

import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)                                             # Datos


plt.hist(ocurrencias, bins=54, edgecolor='purple')                           # Crear el histograma


plt.title('Histograma de vocales ')                                      # Agregar título y etiquetas
plt.xlabel('cantidad')
plt.ylabel('Frecuencia')


plt.show()                                                               # Mostrar la gráfica

'''































#archivos csv:
def mostrar_primeras_filas(ruta): #busca el archivo csv 
    if os.path.exists(ruta):
        archivo = open(ruta, "r", encoding="utf-8") # aca los lee 
        lector = csv.reader(archivo)
        contador = 0
        print("\nPrimeras 15 filas del archivo:\n") #aca es todo el proceso para mostrar las filas 
        for fila in lector:
            print(fila)
            contador += 1
            if contador == 15:
                break
        archivo.close()
    else:
        print("No se encontró el archivo CSV.")

def calcular_estadisticas(ruta): #calculo las estadisticas que me preguntan

    if os.path.exists(ruta):
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo)
        encabezados = next(lector)
        print("\nColumnas disponibles:")
        for i in range(len(encabezados)):
            print(i, "-", encabezados[i])

        col = int(input("Seleccione el número de columna: "))

        datos = []
        for fila in lector:
            try:
                valor = float(fila[col])
                datos.append(valor)
            except:
                pass

        archivo.close()

        if len(datos) > 0:
            promedio = sum(datos) / len(datos)
            minimo = min(datos)
            maximo = max(datos)
            print("\n--- ESTADÍSTICAS ---")
            print("Cantidad de datos:", len(datos))
            print("Promedio:", promedio)
            print("Mínimo:", minimo)
            print("Máximo:", maximo)
        else:
            print("No hay datos numéricos válidos en esa columna.")
    else:
        print("El archivo no existe.")

#grafica la columna numerica que el usuario escoge 
def graficar_columna(ruta):
    if os.path.exists(ruta):
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo)
        encabezados = next(lector)
        print("\nColumnas disponibles:")
        for i in range(len(encabezados)):
            print(i, "-", encabezados[i])

        col = int(input("Seleccione el número de columna numérica: "))

        datos = []
        for fila in lector:
            try:
                valor = float(fila[col])
                datos.append(valor)
            except:
                pass

        archivo.close()

        if len(datos) > 0:
            plt.plot(datos)
            plt.title("Gráfico de columna numérica")
            plt.xlabel("Índice")
            plt.ylabel(encabezados[col])
            plt.show()
        else:
            print("No se pudieron graficar los datos.")
    else:
        print("El archivo no existe o la ruta es incorrecta.")


#menu principal

def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====") #pregunta al usuario las opciones
        print("1. Listar archivos en una ruta")
        print("2. Procesar archivo de texto ")
        print("3. Procesar archivo CSV )")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")#pide que ingrese una opcion 

        if opcion == "1": 
            ruta = input("Ingrese la ruta del directorio: ") #busca los archivos del directorio que el usuario le ponga 
            if os.path.exists(ruta): #busca la ruta si existe 
                archivos = os.listdir(ruta) #define archivos y busca el directorio de la ruta
                print("\nArchivos encontrados:")
                for nombre in archivos:
                    ruta_completa = os.path.join(ruta, nombre) #si el lo que encontro en la ruta es un archivo lo muestra 
                    if os.path.isfile(ruta_completa):
                        print("-", nombre)
            else:
                print("La ruta no existe.")
        elif opcion == "2":
            ruta = input("Ingrese el nombre completo del archivo .txt: ")
            submenu_txt(ruta)
        elif opcion == "3":
            ruta = input("Ingrese el nombre completo del archivo .csv: ")
            submenu_csv(ruta)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")



#submenu del txt

def submenu_txt(ruta):
    while True:
        print("\n--- SUBMENÚ .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Contar ocurrencias")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contar_palabras_y_caracteres(ruta)
        elif opcion == "2":
            reemplazar_palabra(ruta)
        elif opcion == "3":
            contar_ocurrencias(ruta)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

#submenu del csv

def submenu_csv(ruta):
    while True:
        print("\n--- SUBMENÚ .CSV ---")
        print("1. Mostrar primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_primeras_filas(ruta)
        elif opcion == "2":
            calcular_estadisticas(ruta)
        elif opcion == "3":
            graficar_columna(ruta)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

menu_principal() #llama a la funcion principal