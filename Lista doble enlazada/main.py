from lista import Lista
k = Lista()
for dato in range(5):
    k.agregarUltimo(dato)

print(f"Lista: {k}")

k.agregarAntes(3, 5)

print(f"Agregar 5 antes de 3: {k}")

k.agregarDespues(2, 6)

print(f"Agregar 6 despues de 2: {k}")

k.eliminarPrimero()

print(f"Eliminar primero: {k}")

k.eliminarUltimo()

print(f"Eliminar ultimo: {k}")

print(k.buscar(5))

k.eliminar(2)

print(k)
