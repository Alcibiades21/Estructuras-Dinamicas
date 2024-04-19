from lista import Lista

k = Lista()

for dato in range(4):
    k.agregarFinal(dato)

print(k)
print(k.buscar(3))
k.eliminarPrimero()
print(k)
k.elimanrUltimo()
print(k)
