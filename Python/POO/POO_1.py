class Coche():

    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    def estado(self):
        print("El coche tiene",self.ruedas,"ruedas. Un ancho de",self.anchoChasis,
        "y un largo de",self.largoChasis)

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("------A continuación creamos el segundo objeto------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=5
miCoche2.estado()
