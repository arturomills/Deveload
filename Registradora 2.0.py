def en_inventario():
    if agregar in inventario:
        pass
    else:
        print("El articulo no esta en inventario")


inventario = dict(salami=20.00, yuca=15.00, huevo=7.00, cafe=25.00, pan=5.00)
productos = []
agregar = input(str("Que articulo desea comprar: "))
en_inventario()
precio = float(input("costo del articulo : "))
productos.append(agregar)
total = precio
print("Su total a pagar es de ", int(total))
seguir = True

while seguir == True:
    respuesta = input("desea comprar mas articulos ?")

    if respuesta == "si":
        agregar = input("Que mas desea agregar")
        precio = int(input("ingrese el costo"))
        productos.append(agregar)
        total += precio
        print(productos)
        print(total)
    else:
        print(f'pagar el total de {total}')
        print("Gracias por su compra")
