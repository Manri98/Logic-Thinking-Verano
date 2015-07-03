numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce un segundo número mayor que el anterior: "))
while numero2 <= numero1:
    numero2 = int(input("El segundo número DEBE ser mayor que el primero: "))
print("Los números introducidos son ", numero1, " y ",numero2)
