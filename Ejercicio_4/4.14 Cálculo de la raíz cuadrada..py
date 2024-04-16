# Se inicializa x a la unidad.
x = 1.0

# Se solicita al usuario que ingrese el valor de a.
a = float(input("Dame el valor de a: \n"))

# Se inicia el cálculo de la raíz cuadrada de a.
for k in range(1, 10):
    x = (x + a / x) / 2

print("La raíz después de", k, "iteraciones es", x)