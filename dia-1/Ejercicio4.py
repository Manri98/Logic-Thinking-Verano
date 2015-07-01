i = 0
n = 0
#letra = 0
vocales = ["a","e","i","o","u","A","E","I","O","U"]

cadena = input("Introduce una cadena de texto: ")
for letra in range (len(cadena)):
    for n in range (len(vocales)):
        if cadena[i]==vocales[n]:
            print("Es una vocal.")            
        else:
            print("Es una consonante")
    i +=i
