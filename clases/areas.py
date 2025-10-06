import numpy as np

class AreaCirculo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0

    def calcular_area(self):
        self.area = np.pi * (self.radio ** 2)

    def mostrar_resultado(self):
        print(f"El área del círculo es: {self.area:.2f}")
