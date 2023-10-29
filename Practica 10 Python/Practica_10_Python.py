#Brenda Lizeth Palasio Gutiérrez
#Suma Recursiva e Iterativa

def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    suma += n
    return suma

def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

numero = int(input("Ingrese un numero para la suma: "))
opcion = int(input("Elija una opcion (1 para suma recursiva, 2 para suma iterativa): "))

if opcion == 1:
    print("Suma recursiva:", suma_recursiva(numero))
elif opcion == 2:
    print("Suma iterativa:", suma_iterativa(numero))
else:
    print("Opcion no valida.")
