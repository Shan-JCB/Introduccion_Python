import math


def grados_a_radianes(grados):
    return grados * (math.pi / 180)


def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)


try:
    opcion = input("¿Qué conversión desea realizar?\n1. De grados a radianes\n2. De radianes a grados\nOpción: ")
    if opcion not in ["1", "2"]:
        raise ValueError("Opción inválida. Por favor, seleccione 1 o 2.")

    valor = float(input("Ingrese el valor a convertir: "))

    if opcion == "1":
        resultado = grados_a_radianes(valor)
        print(f"{valor} grados sexagesimales son aproximadamente {resultado:.2f} radianes.")
    elif opcion == "2":
        resultado = radianes_a_grados(valor)
        print(f"{valor} radianes son aproximadamente {resultado:.2f} grados sexagesimales.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
