lista = [0]
i = 0

print("Introduzca enteros cada vez mayores, para terminar escriba un número menor que el anterior")
lista[0] = input("Introduce un número: ")
print("DEBUGG")
lista.append(input("Introduce un número: "))
while lista[i] < int(len(lista)):
    print("DEBUGG")
    lista.append(input("Introduce un número: "))
    i += i
