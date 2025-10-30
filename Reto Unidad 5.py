# Se usan los modulos que se van a usar
import os # funciones para interactuar con el sistema operativo, como verificar si un archivo o directorio existe, listar archivos en un directorio, etc.
import csv # lectura y escritura para el archivo csv de forma facil
import matplotlib.pyplot as plt # esta es una libreria para poder graficar datos de manera sencilla





# funcion para contar los caracteres y palabras de este archivo de "txt"
def contar_palabras_y_caracteres(ruta): 
    while True:
        if os.path.exists(ruta):  # Verifica si el archivo existe
            archivo = open(ruta, "r", encoding="utf-8")  # Abre el archivo en modo "r" con ese formato que permite leer caracteres especiales como tildes, eñes, etc.
            texto = archivo.read()  # Lee el contenido de archivo y lo guarda en la variable texto
            archivo.close()  # Cierra el archivo

            palabras = texto.split()  # Divide el texto en palabras
            num_palabras = len(palabras) # se usa " len " para contar las palabras
            num_caracteres = len(texto) # se usa " len " para contar los caracteres osea una letra, numero, simbolo 
            sin_espacios = len(texto.replace(" ", "").replace("\n", "")) # cuenta los caracteres sin espacios ni saltos de linea

            print("\n--- RESULTADOS ---")
            print("Número de palabras:", num_palabras)
            print("Número de caracteres (con espacios):", num_caracteres)
            print("Número de caracteres (sin espacios):", sin_espacios)
            opcion = input("Ingrese 'salir' para volver al submenu: ")
            opcion = opcion.lower()
            if opcion == "salir":
                break

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
        texto = archivo.read() # lee todo el contenido del archivo y lo guarda en la variable texto
        archivo.close() 
        
        texto_nuevo = texto.replace(palabra, nueva)

        archivo = open(ruta, "w", encoding="utf-8") # se abre el archivo en modo escritura "w"  borra los cambios el contenido anteriro  para guardar los cambios nuevos.
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











# funcion para mostrar las primeras 15 filas de un archivo "csv"
def mostrar_primeras_filas(ruta): # muestra las primeras 15 filas de un archivo csv
    if os.path.exists(ruta): # verifica si la ruta existe
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo) # se usa el metodo reader para leer el archivo csv
        contador = 0 # se usa para saber cuantas filas se han demostrado hasta ahora 
        print("\nPrimeras 15 filas del archivo:\n") # Los \n agregan líneas en blanco antes y después para mejor lectura en consola.
        for fila in lector:
            print(fila)
            contador += 1 # incrementa el contador en 1 por cada fila leída para llevar la cuenta
            if contador == 15:
                break
        archivo.close()
    else:
        print("El archivo no existe.")

# funcion para calcular estadisticas de una columna numerica en un archivo csv 
def calcular_estadisticas(ruta):
    if os.path.exists(ruta): # verifica si el archivo existe de la ruta dada
        archivo = open(ruta, "r", encoding="utf-8")
        lector = csv.reader(archivo)
        filas = list(lector)
        archivo.close()

        if not filas: # verifica si el archivo esta vacio o no.
            print("Archivo CSV")
            return

        encabezados = filas[0] # obtiene los encabezados de las columnas del archivo csv

        print("\nColumnas disponibles:")
        for i in range(len(encabezados)): # muestra las columnas disponibles
            print(i, "-", encabezados[i]) # imprime el indice y el nombre de cada columna

        try: # este comando es para que el usario intente ejecutar el codigo y si hay un error, el programa no se caiga
            col = int(input("Seleccione el número de columna: ")) # pide al usuario que seleccione la columna para la cual desea calcular las estadísticas
        except:
            print("Entrada inválida.") 
            return

        datos = [] 
        for fila in filas[1:]: # recorre cada fila del archivo csv tratando de convertir el valor de la columna seleccionada en un número decimal (float).
            if col < len(fila): # verifica que la columna seleccionada exista en la fila actual
                valor = fila[col].strip() # elimina espacios en blanco al inicio y al final del valor
                v_normalizado = valor.replace(',', '.') # reemplaza las comas por puntos para manejar decimales
                # permitir un signo negativo y un solo punto decimal
                tmp = v_normalizado
                if tmp.startswith('-'): # permite numeros negativos
                    tmp = tmp[1:]
                if tmp and tmp.count('.') <= 1 and tmp.replace('.', '', 1).isdigit():
                    try:
                        datos.append(float(v_normalizado))
                    except:
                        pass

        if len(datos) > 0: # si hay datos validos en la columna seleccionada, calcula las estadisticas
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
        for i in range(len(encabezados)): # muestra las columnas disponibles
            print(i, "-", encabezados[i]) # imprime el indice y el nombre de cada columna

        col = int(input("Seleccione el número de columna: "))

        datos = []
        for fila in lector: # se recorre cada fila del archivo csv tratando de convertir el valor de la columna seleccionada en un número decimal (float).
            if col < len(fila): # verifica que la columna seleccionada exista en la fila actual
                valor = fila[col].strip()
                v_normalizado = valor.replace(',', '.')
                # permitir un signo negativo y un solo punto decimal
                tmp = v_normalizado # temporal para hacer las verificaciones
                if tmp.startswith('-'): # permite numeros negativos
                    tmp = tmp[1:]
                if tmp and tmp.count('.') <= 1 and tmp.replace('.', '', 1).isdigit(): # verifica que el valor sea un número válido
                    try:
                        datos.append(float(v_normalizado))
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
        print("A. Contar palabras y caracteres")
        print("B. Reemplazar palabra")
        print("C. Contar ocurrencias")
        print("D. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        opcion = opcion.upper()

        if opcion == "A":
            contar_palabras_y_caracteres(ruta)
        elif opcion == "B":
            reemplazar_palabra(ruta)
        elif opcion == "C":
            contar_ocurrencias(ruta)
        elif opcion == "D":
            break
        else:
            print("Opción no válida.")





# submenú para las funciones de archivo .csv
def submenu_csv(ruta):
    while True:
        print("\n--- SUBMENÚ DE ARCHIVO .CSV ---")
        print("A. Mostrar primeras filas")
        print("B. Calcular estadísticas")
        print("C. Graficar columna")
        print("D. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        opcion = opcion.upper()

        if opcion == "A":
            mostrar_primeras_filas(ruta)
        elif opcion == "B":
            calcular_estadisticas(ruta)
        elif opcion == "C":
            graficar_columna(ruta)
        elif opcion == "D":
            break
        else:
            print("Opción no válida.")






# menú principal del programa
def menu_principal():
    while True:
        print("\n MENÚ PRINCIPAL ")
        print("A. Listar archivos en una ruta")
        print("B. Procesar archivo de texto (.txt)")
        print("C. Procesar archivo CSV (.csv)")
        print("D. Salir")

        opcion = input("Seleccione una opción: ")
        opcion = opcion.upper()

        if opcion == "A": 
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
        elif opcion == "B":
            ruta = input("Ingrese el nombre completo del archivo .txt: ")
            submenu_txt(ruta)
        elif opcion == "C":
            ruta = input("Ingrese el nombre completo del archivo .csv: ")
            submenu_csv(ruta)
        elif opcion == "D":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

menu_principal()

              
              









