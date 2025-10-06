import clases.areas as areas
circulo = areas.AreaCirculo(radio)

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = AreaCirculo(radio)
    circulo.calcular_area()
    circulo.mostrar_resultado()

if __name__ == "__main__":
    main()
