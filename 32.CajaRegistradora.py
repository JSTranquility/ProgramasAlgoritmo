def caja_registradora():
   
    subtotal = 0.0
    IVA_RATE = 0.15

    print("Ingrese los productos y precios. Para finalizar, deje el código de producto en blanco.")
    print("\n----- Recibo de Pago -----\n")

    while True:

        codigo_producto = input("Ingrese código de producto: ")
        if codigo_producto == "":
            break

        try:
            precio = float(input("Ingrese precio del producto: "))
        except ValueError:
            print("Por favor, ingrese un valor válido para el precio.")
            continue

        subtotal += precio

        print(f"Código de Producto: {codigo_producto}, Precio: {precio:.2f}")

    IVA = subtotal * IVA_RATE
    total = subtotal + IVA

    print("\n----- Totales -----")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"IVA (15%): {IVA:.2f}")
    print(f"Total: {total:.2f}")

if __name__ == "__main__":
    caja_registradora()
