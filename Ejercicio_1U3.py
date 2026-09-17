#Ejercicio 1

cliente= ""
while not cliente.isalpha():
    cliente= input("Ingrese el nombre del cliente: ")
productos= ""
while not productos.isdigit() or int(productos) <= 0:
    productos= input("Ingrese la cantidad de productos: ")
productos= int(productos)

con_descuento= 0
sin_descuento= 0

for i in range(productos):
    print(f"Producto {i+1}:")
    precio= ""
    while not precio.isdigit():
        precio= input("Ingrese el precio del producto: ")
    precio= int(precio)

    descuento= ""
    while descuento.lower() not in ["s", "n"]:
        descuento= input("¿El producto tiene descuento? (s/n): ")

    sin_descuento += precio
    if descuento.lower() == "s":
        con_descuento += precio * 0.9
    else:
        con_descuento += precio

print(f"Cliente: {cliente}")
print(f"Cantidad de productos: {productos}")
print(f"Total sin descuento: ${sin_descuento:.2f}")
print(f"Total con descuento: ${con_descuento:.2f}")
print(f"Ahorro total: ${sin_descuento - con_descuento:.2f}")
print(f"Promedio por producto: ${con_descuento / productos:.2f}")