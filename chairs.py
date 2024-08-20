
def CalcularDescuento(tipoCliente, costoTotal):
    descuento = 0
    
    if tipoCliente == "N":
        if costoTotal >= 10000 and costoTotal < 20000:
            descuento = 0.1
        elif costoTotal >= 20000:
            descuento = 0.15
    elif tipoCliente == "F":
        descuento = 0.2
        
    return descuento
            

def TipoDeCliente(cliente):
    if cliente == "N":
        print("Cliente normal seleccionado! \n")
        return "N"
    elif cliente == "F":
        print("Cliente frecuente seleccionado! \n")    
        return "F"
    else:
        print("Cliente invalido \n")
        return 0
        

def TipoDeSilla(silla):
    if silla == "B":
        print("Precio es igual a $700 \n")
        return 700
    elif silla == "E":
        print("Precio es igual a $900 \n")
        return 900
    elif silla == "L":
        print("Precio es igual a $1500 \n")
        return 1500
    else:
        print("Tipo de silla invalido \n")
        return 0


def main():
    
    print("Ingresa el tipo de cliente: ")
    cliente = input()
    tipoDeCliente = TipoDeCliente(cliente)
    if tipoDeCliente == 0:
        return
    
    print("Ingresa tipo de silla: ")
    silla = input()
    costoPorSilla = TipoDeSilla(silla)
    if costoPorSilla == 0:
        return
    
    print("Ingresa cantidad: ")
    cantidad = input()
    costoTotal = costoPorSilla * int(cantidad)
    
    descuento = CalcularDescuento(tipoDeCliente, costoTotal)
    
    precioConDescuento = costoTotal - (costoTotal * descuento)
    
    print(f"\n\nPrecio antes de descuento: ${costoTotal}")
    print(f"Descuento total: %{descuento * 100}")
    print(f"Precio despues del descuento: ${precioConDescuento}")
    
main()