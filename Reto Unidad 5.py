# Se usan losmodulos que se van a usar
import os
import csv 
import matplotlib.pyplot as plt

# funcion para contar los caracteres y palabras de este archivo de texto
def contar_palabras_y_caracteres(ruta):
    if os.path.exists(ruta):  # Verifica si el archivo existe
        archivo = open(ruta, "r", encoding="utf-8")  # Abre el archivo en modo "r" con ese formato que permite leer caracteres especiales como tildes, eñes, etc.
        texto = archivo.read()  # Lee el contenido
        archivo.close()  # Cierra el archivo

        palabras = texto.split()  # Divide el texto en palabras
        num_palabras = len(palabras) # se usa " len " para contar las palabras
        num_caracteres = len(texto) # se usa " len " para contar los caracteres
        sin_espacios = len(texto.replace(" ", "").replace("\n", "")) # cuenta los caracteres sin espacios ni saltos de linea

        print("\n--- RESULTADOS ---")
        print("Número de palabras:", num_palabras)
        print("Número de caracteres (con espacios):", num_caracteres)
        print("Número de caracteres (sin espacios):", sin_espacios)

        # Datos para la gráfica
        categorias = ['Palabras', 'Caracteres', 'Sin Espacios'] #contiene los nombres que se mostrarán en el eje X (las etiquetas).
        valores = [num_palabras, num_caracteres, sin_espacios] #contiene los números correspondientes

        # Gráfica de barras
        plt.bar(categorias, valores) # se usa el comando "plt.bar" para crear la grafica de barras
        # Agregar título y etiquetas
        plt.title("Conteo de texto")
        plt.xlabel("Categorías")
        plt.ylabel("Valores")
        plt.show() # Mostrar la gráfica

    else: # si no existe la ruta
        print("El archivo no existe.") # Si el archivo no se encuentra (la condición del if no se cumple), se imprime un mensaje de error.


def reemplazar_palabra(ruta): # funcionn para reemplazar palabras de este archivo de texto
    if os.path.exists(ruta): # esto es para ver si la ruta existe y en dado caso que no exista genere un mensaje de error
        palabra = input("Palabra a reemplazar: ")
        nueva = input("Nueva palabra: ")

        archivo = open(ruta, "r", encoding="utf-8") # encoding="utf-8" se usa para que el programa entienda caracteres especiales, como tildes (á, é, í) o la
        texto = archivo.read()
        archivo.close()

        texto_nuevo = texto.replace(palabra, nueva)

        archivo = open(ruta, "w", encoding="utf-8") # se abre el archivo en modo escritura "w"  borra os cambios el contenido anteriro  para guardar los cambios nuevos.
        archivo.write(texto_nuevo)
        archivo.close()

        print("Palabra reemplazada correctamente.") # Si todo sale bien, se imprime un mensaje de confirmación para que el usario lo vea y confirme.
    
    else:
        print("El archivo no existe.")

# funcion para contar cuantas veces aparece una palabra en el texto 
def contar_ocurrencias(ruta): # define la funcion de contar ocurrencias que ayuda a saber cuantas veces se dice una palabra en el archivo
    if os.path.exists(ruta): 
        while True: # bucle infinito para que el usuario pueda contar varias palabras sin tener que reiniciar el programa
            palabra = input("Ingrese la palabra para contar (o 'salir' para terminar): ")
            if palabra.lower() == "salir": # si el usario no quiere contar ninguna palabra mas, puede escribir "salir" y el programa se detiene
                break

            archivo = open(ruta, "r", encoding="utf-8")
            texto = archivo.read().lower() # convierte todo el texto a minúsculas para que la búsqueda no sea sensible a mayúsculas o minúsculas
            archivo.close()

            lista = texto.split() # divide el texto completo en una lista de palabras, separando por espacios o saltos de línea.
            conteo = lista.count(palabra.lower()) # se usa para saber cuantas veces aparece la palabra en el texto y tambien para pasar las palabras a Minusculas.

            print(f"La palabra '{palabra}' aparece {conteo} veces.\n")
    else:
        print("El archivo no existe.")

# funcion para mostrar las primeras 15 filas de un archivo csv
def mostrar_primeras_filas(ruta): # muestra las primeras 15 filas de un archivo csv
    if os.path.exists(ruta): # verifica si la ruta existe
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo) # se usa el metodo reader para leer el archivo csv
        contador = 0 # se usa para saber cuantas filas se han demostrado hasta ahora 
        print("\nPrimeras 15 filas del archivo:\n") # Los \n agregan líneas en blanco antes y después para mejor lectura en consola.
        for fila in lector:
            print(fila)
            contador += 1
            if contador == 15:
                break
        archivo.close()
    else:
        print("El archivo no existe.")

# funcion para calcular estadisticas de una columna numerica en un archivo csv 
def calcular_estadisticas(ruta):
    if os.path.exists(ruta): # verifica si el archivo existe de la ruta dada
        archivo = open(ruta, "r", encoding="utf-8") 
        lector = csv.reader(archivo) #Usa la función csv.reader() para leer el archivo CSV línea por línea y convertir cada línea en una lista (cada columna es un elemento).
        encabezados = next(lector) # se usa "next " para leer la primera linea del archivo

        print("\nColumnas disponibles:")
        for i in range(len(encabezados)): # se usa este bucle for para mostrar las columnas disponibles en el archivo csv
            print(i, "-", encabezados[i])

        col = int(input("Seleccione el número de columna: ")) # Pide al usuario que escriba el número de la columna que desea analizar, y lo convierte a número entero (int).

        datos = []
        for fila in lector:
            try:
                valor = float(fila[col]) # intenta convertir el valor de la columna seleccionada con "fila" en un número decimal (float).
                datos.append(valor) # si la conversión es exitosa, agrega el valor a la lista "datos"
            except:
                pass

        archivo.close()

        if len(datos) > 0:
            promedio = sum(datos) / len(datos)
            minimo = min(datos)
            maximo = max(datos)
            # muestra los resultados de manera clara y ordenada
            print("\n--- ESTADÍSTICAS ---")
            print("Cantidad de datos:", len(datos))
            print("Promedio:", promedio)
            print("Mínimo:", minimo)
            print("Máximo:", maximo)
        else:
            print("No hay datos numéricos válidos en esa columna.")
    else:
        print("El archivo no existe.")

# funcion para graficar una columna numerica de un archivo csv
def graficar_columna(ruta):
    if os.path.exists(ruta):
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo) # Usa la función csv.reader() para leer el archivo línea por línea y separarlo por comas (,), como una lista de listas.
        encabezados = next(lector) # Usa la función csv.reader() para leer el archivo línea por línea y separarlo por comas (,), como una lista de listas.

        print("\nColumnas disponibles:")
        for i in range(len(encabezados)):
            print(i, "-", encabezados[i])

        col = int(input("Seleccione el número de columna: "))

        datos = []
        for fila in lector: # se recorre cada fila del archivo csv tratando de convertir el valor de la columna seleccionada en un número decimal (float).
            try:
                valor = float(fila[col])
                datos.append(valor)
            except:
                pass

        archivo.close()

        if len(datos) > 0:
            plt.plot(datos) # Usa Matplotlib para crear un gráfico de línea con los valores de la columna seleccionada.
            plt.title("Gráfico de columna numérica")
            plt.xlabel("Índice")
            plt.ylabel(encabezados[col])
            plt.show()
        else:
            print("No se pudieron graficar los datos.")
    else:
        print("El archivo no existe.")

# submenú para las funciones de archivo .txt
def submenu_txt(ruta):
    while True:
        print("\n--- SUBMENÚ DE ARCHIVO .TXT ---")
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

# submenú para las funciones de archivo .csv
def submenu_csv(ruta):
    while True:
        print("\n--- SUBMENÚ DE ARCHIVO .CSV ---")
        print("1. Mostrar primeras filas")
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

# menú principal del programa
def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Listar archivos en una ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo CSV (.csv)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1": 
            ruta = input("Ingrese la ruta del directorio: ")
            if os.path.exists(ruta):
                archivos = os.listdir(ruta)
                print("\nArchivos encontrados:")
                for nombre in archivos:
                    ruta_completa = os.path.join(ruta, nombre)
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

menu_principal()

              
              









