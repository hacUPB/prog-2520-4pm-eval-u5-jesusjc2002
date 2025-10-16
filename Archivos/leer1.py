#1 abrir el archivo
fp = open("C:\\Users\\jesus david\\OneDrive\\Escritorio\\TextoR.txt", "r", encoding="utf-8")           
#2 leer el archivo
datos = fp.read(20)
datos = fp.read()
fp.readlines()
fp.read(5)
dato = fp.readline(7)
#3. Cerrar el archivo
fp.close()
for line in fp:
    print(line[0],end="")


fp.close()







print(datos)