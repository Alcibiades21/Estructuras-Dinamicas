from nodo import Nodo


class Lista:
    primero = None
    ultimo = None

    def agregarPrimero(self, x):
        nuevo = Nodo(x)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def agregarFinal(self, x):
        nuevo = Nodo(x)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
        else:
            self.ultimo.siguiente = nuevo
            nuevo.siguiente = self.primero
            self.ultimo = nuevo

    def eliminarPrimero(self):
        if self.primero != None:
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                self.primero = self.primero.siguiente
                self.ultimo.siguiente = self.primero

    def elimanrUltimo(self):
        if self.primero != None:
            if self.primero == self.ultimo:
                self.primero = None
                self.ultimo = None
            else:
                aux = self.primero
                while aux.siguiente != self.ultimo:
                    aux = aux.siguiente
                self.ultimo = aux
                self.ultimo.siguiente = self.primero

    def buscar(self, x):
        if self.primero == None:
            return None
        aux = self.primero
        sw = True
        while sw == True:
            if aux.dato == x:
                return aux
            aux = aux.siguiente
            if aux == self.primero:
                return None

    def __str__(self) -> str:
        aux = self.primero
        lista = ""
        sw = True
        while sw == True:
            lista += str(aux.dato) + " "
            aux = aux.siguiente
            if aux == self.primero:
                return lista
