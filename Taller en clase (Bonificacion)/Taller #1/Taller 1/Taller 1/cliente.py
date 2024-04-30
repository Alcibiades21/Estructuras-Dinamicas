from nodo import *

prim = None
arch = open(
    'c:/Users/Alcibiades Lopez/Desktop/Estructura de datos/Estructuras dináminas/Ejercicio en clases/clientes.csv')
si = False
for lin in arch:

    try:
        datos = lin.strip().split(";")
        nuevo = Cliente(
            datos[0],
            datos[1],
            datos[2],
            int(datos[3]),
            int(datos[4])
        )
        nuevo.enlace = prim
        prim = nuevo
    except:
        pass

op = 0
while op != 5:
    op = int(input("1. Mostrar el total\n2. Buscar por fecha\n3. Buscar por cliente\n4. Buscar por producto\n5. Salir\n-->> "))
    if op == 1:
        cont = 0
        zum = 0
        aux = prim
        while aux != None:
            cont += 1
            zum += aux.valor
            aux = aux.enlace
        print(f"Cantidad de registros: {
              cont}\nTotal de cantidades por valor unitario: {zum}\n")

    if op == 2:
        fec = input("Ingrese fecha a buscar: ")
        aux = prim
        while aux != None:
            if fec == aux.fecha:
                print(aux)
            aux = aux.enlace

    if op == 3:
        aux = prim
        cli = input("Nombre del cliente a buscar: ")
        while aux != None:
            if aux.cliente == cli:
                print(aux)
            aux = aux.enlace

    if op == 4:
        aux = prim
        prod = input("Nombre del producto a buscar: ")
        while aux != None:
            if aux.producto == prod:
                print(aux)
            aux = aux.enlace
