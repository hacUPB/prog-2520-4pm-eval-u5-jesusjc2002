try:
     entero = int(input("Ingrese un número entero: "))
except ValueError:
    print("El valor ingresado no es un numero. ") 
else:
    print("La operación se realizó correctamente.")
    print(entero)
finally: 
    print("Puedes continuar con el programa.")


print(entero)
