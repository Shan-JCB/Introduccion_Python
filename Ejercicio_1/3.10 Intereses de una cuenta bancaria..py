def calcular_saldo_final(saldo):
    if saldo < 10000.00:
        saldo_final = saldo * (1 + 0.03)
    else:
        saldo_final = saldo * (1 + 0.04)
    return saldo_final

def main():
    print("Bienvenido al sistema de cálculo de saldo final.")
    while True:
        try:
            saldo_actual = float(input("Por favor, ingrese su saldo actual: "))
            if saldo_actual < 0:
                print("El saldo no puede ser negativo. Por favor, intente de nuevo.")
            else:
                saldo_final = calcular_saldo_final(saldo_actual)
                print("Su saldo final es: %.2f" % saldo_final)
                break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()