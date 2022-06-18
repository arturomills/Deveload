inventario: dict[str, int] = {"salami": 25, "pan": 5, "huevo": 6}
lista_productos = []
def ingreso_producto():

    continuar = True

    while continuar == True:
        total = 0
        ingresar_producto = str(input("Que desea Comprar ? : "))

        if ingresar_producto in inventario:

            lista_productos.append(ingresar_producto)
            ingresar_cantidad = int(input("Cantidad del articulo : "))
            total = inventario.get(ingresar_producto) * ingresar_cantidad
            print (f'Usted ha selccioando {ingresar_cantidad}  {lista_productos} a un precio de {inventario.get(ingresar_producto)} y el total a pagar es {total}')
            seguir_comprando = input("Desea continuar comprando ? ")

            continuar = False

        else :
            print("El articulo no esta en inventario")
            print('Hello')
            continuar = True

ingreso_producto()