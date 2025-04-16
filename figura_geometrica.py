"""
Este script contiene una clases que permite calcular las áreas de distintas figuras geométricas.
"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """
    Clase abstracta que define la interfaz para calcular áreas.
    """
    @abstractmethod
    def calcular_area(self):
        """
        Método abstracto para calcular el área de una figura.
        """
    def verificar_entrada(self):
        """
        Método que verifica si la entrada de variables es correcta.
        """


class Rectangulo(FiguraGeometrica):
    """
    Clase abstracta que define la interfaz para calcular el áre a de un rectángulo.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Calcula el área del rectángulo.
        """
        area = self.base * self.altura
        return area


class Triangulo(FiguraGeometrica):
    """
    Clase abstracta que define la interfaz para calcular el áre a de un triángulo.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Calcula el área del triángulo.
        """
        area = (self.base * self.altura)/2
        return area


class Circulo(FiguraGeometrica):
    """
    Clase abstracta que define la interfaz para calcular el áre a de un circulo.
    """
    def __init__(self, radio):
        self.pi = 3.14159
        self.radio = radio

    def calcular_area(self):
        """
        Calcula el área del círculo.
        """
        area = self.pi * (self.radio ** 2)
        return area


# Variables globales
BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3

# Ejecución principal
if __name__ == "__main__":
    # Crear instancias de las figuras
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    # Calcular áreas
    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
