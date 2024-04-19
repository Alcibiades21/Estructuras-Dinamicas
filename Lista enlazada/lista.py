from nodo import Nodo


class Lista:
    primero = None

    def agregarPrimero(self, x):
        nuevo = Nodo(x)
        if self.primero != None:
            nuevo.siguiente = self.primero
        self.primero = nuevo

    def agregarFinal(self, x):
        nuevo = Nodo(x)
        if self.primero == None:
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = nuevo

    def __str__(self) -> str:
        aux = self.primero
        lista = ""
        while aux != None:
            lista += str(aux.dato) + " "
            aux = aux.siguiente
        return lista
