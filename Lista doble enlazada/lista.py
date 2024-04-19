from nodo import Nodo


class Lista:
    primero = None
    ultimo = None

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        aux = self.primero
        lista = ""
        while aux != None:
            lista += str(aux.dato) + " "
            aux = aux.derecha
        return lista

    def agregarUltimo(self, x):
        nuevo = Nodo(x)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.derecha = nuevo
            nuevo.izquierda = self.ultimo
            self.ultimo = nuevo

    def agregarPrimero(self, x):
        nuevo = Nodo(x)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.primero.izquierda = nuevo
            nuevo.derecha = self.primero
            self.primero = nuevo

    def eliminarPrimero(self):
        if self.primero == None:
            return False
        else:
            if self.primero == self.ultimo:
                self.primero = self.ultimo = None
            else:
                aux = self.primero
                self.primero = aux.derecha
                aux.derecha = None
                self.primero.izquierda = None
            return True

    def eliminarUltimo(self):
        if self.primero == None:
            return None
        else:
            if self.primero == self.ultimo:
                self.primero = self.ultimo = None
            else:
                aux = self.ultimo
                self.ultimo = aux.izquierda
                aux.izquierda = None
                self.ultimo.derecha = None
            return True

    def buscar(self, x):
        aux = self.primero
        sw = 0
        while sw == 0 and aux != None:
            if aux.dato == x:
                sw = 1
            else:
                aux = aux.derecha
        return aux

    def eliminar(self, x):
        aux = self.buscar(x)
        if aux == None:
            return False
        else:
            if aux == self.primero:
                self.eliminarPrimero()
            elif aux == self.ultimo:
                self.eliminarUltimo()
            else:
                ant = aux.izquierda
                pos = aux.derecha
                aux.derecha = None
                aux.izquierda = None
                ant.derecha = pos
                pos.izquierda = ant
            return True

    def agregarAntes(self, x, y):
        aux = self.buscar(x)
        if aux == None:
            return False
        else:
            if aux == self.primero:
                self.eliminarPrimero()
            elif aux == self.agregarUltimo:
                self.eliminarUltimo()
            else:
                nuevo = Nodo(y)
                ant = aux.izquierda
                ant.derecha = nuevo
                nuevo.derecha = aux
                aux.izquierda = nuevo
                nuevo.izquierda = ant
            return True

    def agregarDespues(self, x, y):
        aux = self.buscar(x)
        if aux == None:
            return False
        else:
            if aux == self.ultimo:
                self.agregarUltimo(y)
            else:
                nuevo = Nodo(y)
                pos = aux.derecha
                pos.izquierda = nuevo
                nuevo.izquierda = aux
                aux.derecha = nuevo
                nuevo.derecha = pos
            return True
