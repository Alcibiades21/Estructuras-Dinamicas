class Cliente:
    def __init__(self, fec, cli, nom, cant, valor) -> None:
        self.fecha = fec
        self.cliente = cli
        self.producto = nom
        self.cantidad = cant
        self.valor = valor
        self.enlace = None

    def __str__(self) -> str:
        return f"{self.fecha} {self.cliente} {self.producto} {str(self.cantidad)} {str(self.valor)}"

    def total(self):
        return self.valor * self.cant
