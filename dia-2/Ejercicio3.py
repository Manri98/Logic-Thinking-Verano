contrasena = 1234
intento = 0
while intento != contrasena:
    intento = int(input("Introduzca una contraseña numérica: "))
    if intento == contrasena:
        print("Bienvenido!")
        break
    print("ERROR")
