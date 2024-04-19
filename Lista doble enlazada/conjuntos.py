from lista import Lista
from random import randint

a = Lista()
b = Lista()
n = randint(10, 20)
for i in range(n):
    a.agregarUltimo(randint(50, 99))
m = randint(10, 20)
for i in range(m):
    b.agregarUltimo(randint(50, 99))

print(f"{a}\n{b}")

def union(l1, l2):
    aux = l1.primero
    u = Lista()
    while aux != None:
        if u.buscar(aux.dato) == None:
            u.agregarUltimo(aux.dato)
        aux = aux.derecha


    aux = l2.primero
    l = Lista()
    
    while aux != None:
        if l2.buscar(aux.dato) != None and l.buscar(aux.dato) == None:
            l.agregarUltimo(aux.dato)
        aux = aux.derecha
    return u #se devuelve la unino sin datos repetidos

def interseccion(l1, l2):
    aux = l1.primero
