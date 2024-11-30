def calcular_pago_entradas(cantidad_entradas, precio_entrada):

    if cantidad_entradas == 1:
        return cantidad_entradas * precio_entrada  
    elif cantidad_entradas == 2:
        descuento = 0.10  
    elif cantidad_entradas == 3:
        descuento = 0.15  
    elif cantidad_entradas == 4:
        descuento = 0.20  
    else:
        print("Solo se pueden comprar hasta 4 entradas.")
        return None
    
   
    precio_total = cantidad_entradas * precio_entrada
    precio_con_descuento = precio_total * (1 - descuento)
    
    return precio_con_descuento


precio_entrada = float(input("Ingrese el precio de una entrada: "))
cantidad_entradas = int(input("Ingrese la cantidad de entradas (1-4): "))

monto_a_pagar = calcular_pago_entradas(cantidad_entradas, precio_entrada)

if monto_a_pagar is not None:
    print(f"El monto a pagar por {cantidad_entradas} entradas es: {monto_a_pagar:.2f} unidades monetarias.")
