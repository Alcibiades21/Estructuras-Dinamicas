from lista import Lista
from random import randint

l = Lista()

for dato in range(6):
    l.agregarPrimero(dato)

print(f"Lista actual: {l}")

o = 0

while resp == 0:
    print("Elge una opción:\n")
    o = int(input("1.Eliminar primero\n2.Eliminar ultimo\n3. Agregar antes\n4. Agregar despues\n5.Buscar\n6. Eliminar\n7. Salir"))

    if o == 1:
        l.eliminarPrimero()
        print(f"Se eliminó el valor {} ")
    elif o == 2:
        l.eliminarUltimo()
    elif 0 == 3:
        a = 0
