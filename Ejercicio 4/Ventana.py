class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=0, y2=0):
        self.titulo = titulo
        self.x1 = max(0, x1)
        self.y1 = max(0, y1)
        self.x2 = min(500, x2)
        self.y2 = min(500, y2)

    def getTitulo(self):
        return self.titulo

    def alto(self):
        return self.y2 - self.y1

    def ancho(self):
        return self.x2 - self.x1

    def moverDerecha(self, desplazamiento=1):
        self.x1 += desplazamiento
        self.x2 += desplazamiento
        self.x1 = min(self.x1, 500 - self.ancho())
        self.x2 = min(self.x2, 500)

    def moverIzquierda(self, desplazamiento=1):
        self.x1 -= desplazamiento
        self.x2 -= desplazamiento
        self.x1 = max(self.x1, 0)
        self.x2 = max(self.x2, self.ancho())

    def bajar(self, desplazamiento=1):
        self.y1 += desplazamiento
        self.y2 += desplazamiento
        self.y1 = min(self.y1, 500 - self.alto())
        self.y2 = min(self.y2, 500)

    def subir(self, desplazamiento=1):
        self.y1 -= desplazamiento
        self.y2 -= desplazamiento
        self.y1 = max(self.y1, 0)
        self.y2 = max(self.y2, self.alto())

    def mostrar(self):
        print('Título:', self.titulo)
        print('Coordenadas del vértice superior izquierdo: ({}, {})'.format(self.x1, self.y1))
        print('Coordenadas del vértice inferior derecho: ({}, {})'.format(self.x2, self.y2))
        print()