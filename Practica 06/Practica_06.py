#Brenda Lizeth Palasio Guti�rrez
#Practica 06 - Vectores: Arreglo de Aves e incersi�n de elementos

#Declara una lista de cadenas
aves = ["Loro gris", "Paloma de diamante", "Coctel"]
print("Los valores de la lista antes de insertar: ")

#Itera sobre la lista para imptimir los valores
for ave in aves:
    print(ave,end=" ")

print("\n")

#Agregar tres valores al final de la lista utilizando el m�todo append()
aves.append("Mayna")
aves.append("Periquitos")
aves.append("Cacatua")
print("Los valores de la lista despues de insertar: ")

#Itera sobre la lista para imprimier los valores
for ave in aves:
    print(ave,end=" ")

print("\n")
