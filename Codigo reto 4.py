import os
import csv
import matplotlib.pyplot as plt


# -------------------- LISTA PARA GUARDAR HISTORIAL DE ACCIONES --------------------
historial_acciones = []  # se guardarán todas las acciones realizadas por el usuario


# función para contar los caracteres y palabras de un archivo .txt
def contar_palabras_y_caracteres(ruta): 
    while True:
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as archivo:
                texto = archivo.read()

            palabras = texto.split()
            num_palabras = len(palabras)
            num_caracteres = len(texto)
            sin_espacios = len(texto.replace(" ", "").replace("\n", ""))

            print("\n--- RESULTADOS ---")
            print("Número de palabras:", num_palabras)
            print("Número de caracteres (con espacios):", num_caracteres)
            print("Número de caracteres (sin espacios):", sin_espacios)

            # Registrar en historial
            historial_acciones.append(f"Conteo de palabras/caracteres en {ruta}")

            opcion = input("Ingrese 'salir' para volver al submenu: ").lower()
            if opcion == "salir":
                break

            categorias = ['Palabras', 'Caracteres', 'Sin Espacios']
            valores = [num_palabras, num_caracteres, sin_espacios]

            plt.bar(categorias, valores)
            plt.title("Conteo de texto")
            plt.xlabel("Categorías")
            plt.ylabel("Valores")
            plt.show()

        else:
            print("El archivo no existe.")


# reemplazar una palabra dentro del archivo .txt
def reemplazar_palabra(ruta):
    if os.path.exists(ruta):
        palabra = input("Palabra a reemplazar: ")
        nueva = input("Nueva palabra: ")

        with open(ruta, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

        texto_nuevo = texto.replace(palabra, nueva)

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto_nuevo)

        print("Palabra reemplazada correctamente.")

        # registrar acción en lista historial
        historial_acciones.append(f"Reemplazo '{palabra}' por '{nueva}' en {ruta}")

    else:
        print("El archivo no existe.")


# función para contar cuántas veces aparece una palabra en el texto
def contar_ocurrencias(ruta):
    if os.path.exists(ruta):
        while True:
            palabra = input("Ingrese la palabra para contar (o 'salir' para terminar): ")
            if palabra.lower() == "salir":
                break

            with open(ruta, "r", encoding="utf-8") as archivo:
                texto = archivo.read().lower()

            lista = texto.split()
            conteo = lista.count(palabra.lower())

            print(f"La palabra '{palabra}' aparece {conteo} veces.\n")

            historial_acciones.append(f"Conteo de ocurrencias de '{palabra}' en {ruta}")
    else:
        print("El archivo no existe.")



# función para mostrar primeras 15 filas de un archivo csv
def mostrar_primeras_filas(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            print("\nPrimeras 15 filas del archivo:\n")
            for i, fila in enumerate(lector):
                print(fila)
                if i == 14:
                    break

        historial_acciones.append(f"Se mostraron primeras 15 filas de {ruta}")

    else:
        print("El archivo no existe.")



# función para calcular estadísticas de una columna numérica
def calcular_estadisticas(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)

        if not filas:
            print("Archivo CSV vacío.")
            return

        encabezados = filas[0]

        print("\nColumnas disponibles:")
        for i in range(len(encabezados)):
            print(i, "-", encabezados[i])

        try:
            col = int(input("Seleccione el número de columna: "))
        except:
            print("Entrada inválida.")
            return

        datos = []

        for fila in filas[1:]:
            if col < len(fila):
                valor = fila[col].strip().replace(',', '.')
                tmp = valor
                if tmp.startswith('-'):
                    tmp = tmp[1:]
                if tmp and tmp.count('.') <= 1 and tmp.replace('.', '', 1).isdigit():
                    try:
                        datos.append(float(valor))
                    except:
                        pass

        if datos:

            # ---------------- DICCIONARIO PARA ESTADÍSTICAS ----------------
            estadisticas = {
                "cantidad": len(datos),
                "promedio": sum(datos) / len(datos),
                "minimo": min(datos),
                "maximo": max(datos)
            }

            print("\n--- ESTADÍSTICAS ---")
            print("Cantidad de datos:", estadisticas["cantidad"])
            print("Promedio:", estadisticas["promedio"])
            print("Mínimo:", estadisticas["minimo"])
            print("Máximo:", estadisticas["maximo"])

            historial_acciones.append(f"Estadísticas calculadas en columna {col} del CSV {ruta}")

        else:
            print("No hay datos numéricos válidos en esa columna.")



# función para graficar una columna numérica del csv
def graficar_columna(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezados = next(lector)

        print("\nColumnas disponibles:")
        for i in range(len(encabezados)):
            print(i, "-", encabezados[i])

        col = int(input("Seleccione el número de columna: "))

        datos = []

        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for fila in lector:
                if col < len(fila):
                    valor = fila[col].strip().replace(",", ".")
                    tmp = valor
                    if tmp.startswith("-"):
                        tmp = tmp[1:]
                    if tmp and tmp.count(".") <= 1 and tmp.replace(".", "", 1).isdigit():
                        datos.append(float(valor))

        if datos:
            plt.plot(datos)
            plt.title("Gráfico de columna numérica")
            plt.xlabel("Índice")
            plt.ylabel(encabezados[col])
            plt.show()

            historial_acciones.append(f"Gráfica generada de columna {col} en {ruta}")

        else:
            print("No se pudieron graficar los datos.")
    else:
        print("El archivo no existe.")



# --------------------- TUPLA PARA MENÚ PRINCIPAL ---------------------
opciones_menu = (
    "Listar archivos en una ruta",
    "Procesar archivo TXT",
    "Procesar archivo CSV",
    "Salir"
)
# Esta tupla es INMUTABLE y garantiza que el menú principal no pueda alterarse accidentalmente.



# submenú txt
def submenu_txt(ruta):
    while True:
        print("\n--- SUBMENÚ DE ARCHIVO .TXT ---")
        print("A. Contar palabras y caracteres")
        print("B. Reemplazar palabra")
        print("C. Contar ocurrencias")
        print("D. Volver al menú principal")

        opcion = input("Seleccione una opción: ").upper()

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



# submenú csv
def submenu_csv(ruta):
    while True:
        print("\n--- SUBMENÚ DE ARCHIVO .CSV ---")
        print("A. Mostrar primeras filas")
        print("B. Calcular estadísticas")
        print("C. Graficar columna")
        print("D. Volver al menú principal")

        opcion = input("Seleccione una opción: ").upper()

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



# menú principal
def menu_principal():
    while True:
        print("\n MENÚ PRINCIPAL ")

        # Mostrar la TUPLA del menú
        for i, opcion in enumerate(opciones_menu):
            print(f"{chr(65+i)}. {opcion}")

        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            ruta = input("Ingrese la ruta del directorio: ")
            if os.path.exists(ruta):
                archivos = os.listdir(ruta)
                print("\nArchivos encontrados:")
                for nombre in archivos:
                    ruta_completa = os.path.join(ruta, nombre)
                    if os.path.isfile(ruta_completa):
                        print("-", nombre)
                historial_acciones.append(f"Listado de archivos en {ruta}")
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
            print("\nHistorial de acciones realizadas:")
            for accion in historial_acciones:
                print(" -", accion)
            break

        else:
            print("Opción no válida.")


menu_principal()


