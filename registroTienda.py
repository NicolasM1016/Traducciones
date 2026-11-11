producto = input("Ingrese el nombre del producto (FIN para terminar): ")


cantidad = 0
productosRegistrados = 0
productosConDescuento = 0

totalCompras = 0.0
totalPagado = 0.0

while producto != "FIN":

    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))

    productosRegistrados += 1

    totalProducto = cantidad * precio
    descuento = 0.0

    if totalProducto >= 100000:
        descuento = totalProducto * 0.10
        productosConDescuento += 1

    elif totalProducto >= 50000:
        descuento = totalProducto * 0.05
        productosConDescuento += 1

    valorFinal = totalProducto - descuento

    print("\nProducto: ", producto)
    print("Valor original: $", totalProducto)
    print("Descuento: $", descuento)
    print("Valor a pagar: $", valorFinal)

    totalCompras += totalProducto
    totalPagado += valorFinal

    print()
    producto = input("Ingrese el nombre del producto (FIN para terminar): ")


print("\n--- RESUMEN DE LA COMPRA ---")
print("Productos registrados: ", productosRegistrados)
print("Productos con descuento: ", productosConDescuento)
print("Valor original de las compras: $", totalCompras)
print("Valor final a pagar: $", totalPagado)