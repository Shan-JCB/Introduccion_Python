N = int(input("Escribe la dimensión N>= 2 del cuadrado a dibujar: "))

# Escribe la primera línea de asteriscos.
for i in range(N):
    print("*", end=" ")
print()

# Dibuja las partes laterales
j = 1
while j < N-1:
    for k in range(N):
        if k == 0 or k == N-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    j += 1

# Dibuja el lado de abajo.
for i in range(N):
    print("*", end=" ")
print()