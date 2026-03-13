# -----------------------------------------------------------
# SISTEMA BÁSICO DE GESTIÓN DE INVENTARIO Y PEDIDOS
# -----------------------------------------------------------
# Este programa permite:
# 1. Registrar productos o pedidos
# 2. Mostrar productos o pedidos
# 3. Editar productos o pedidos
# 4. Eliminar productos o pedidos

# Lista que almacenará los productos del inventario
inventario = []

# Lista que almacenará los pedidos
pedidos = []

# FUNCIONES DE INVENTARIO

# FUNCIÓN: registrar un nuevo producto
def registrar_producto():

    print("\n--- Registrar Producto ---")

    # Entrada de datos del usuario
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en inventario: "))

    # Se crea un diccionario para representar el producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Se agrega el producto a la lista de inventario
    inventario.append(producto)

    print("Producto registrado correctamente.")

# FUNCIÓN: mostrar todos los productos
def mostrar_productos():

    print("\n--- Inventario Actual ---")

    # Si no hay productos registrados
    if len(inventario) == 0:
        print("No hay productos registrados.")
        return

    # Se recorre la lista de productos
    for i, producto in enumerate(inventario):

        print("ID:", i)
        print("Nombre:", producto["nombre"])
        print("Precio:", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("-------------------------")

# FUNCIÓN: editar un producto existente
def editar_producto():

    print("\n--- Editar Producto ---")
    mostrar_productos()
    if len(inventario) == 0:
        return

    # Se solicita el ID del producto a editar
    indice = int(input("Ingrese el ID del producto a editar: "))

    # Verificación de que el ID exista
    if indice >= 0 and indice < len(inventario):

        # Nuevos datos
        nombre = input("Nuevo nombre: ")
        precio = float(input("Nuevo precio: "))
        cantidad = int(input("Nueva cantidad: "))

        # Actualización de datos
        inventario[indice]["nombre"] = nombre
        inventario[indice]["precio"] = precio
        inventario[indice]["cantidad"] = cantidad

        print("Producto actualizado correctamente.")
    else:
        print("ID no válido.")


# FUNCIÓN: eliminar producto
def eliminar_producto():

    print("\n--- Eliminar Producto ---")
    mostrar_productos()
    if len(inventario) == 0:
        return
    indice = int(input("Ingrese el ID del producto a eliminar: "))

    if indice >= 0 and indice < len(inventario):
        inventario.pop(indice)
        print("Producto eliminado correctamente.")
    else:
        print("ID no válido.")


# -----------------------------------------------------------
# FUNCIONES DE PEDIDOS
# -----------------------------------------------------------

# FUNCIÓN: registrar pedido
def registrar_pedido():

    print("\n--- Registrar Pedido ---")

    cliente = input("Nombre del cliente: ")
    producto = input("Producto solicitado: ")
    cantidad = int(input("Cantidad del pedido: "))

    pedido = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)
    print("Pedido registrado correctamente.")


# FUNCIÓN: mostrar pedidos
def mostrar_pedidos():

    print("\n--- Lista de Pedidos ---")
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    for i, pedido in enumerate(pedidos):

        print("ID:", i)
        print("Cliente:", pedido["cliente"])
        print("Producto:", pedido["producto"])
        print("Cantidad:", pedido["cantidad"])
        print("-------------------------")


# FUNCIÓN: editar pedido
def editar_pedido():

    print("\n--- Editar Pedido ---")
    mostrar_pedidos()
    if len(pedidos) == 0:
        return
    indice = int(input("Ingrese el ID del pedido a editar: "))
    if indice >= 0 and indice < len(pedidos):
        cliente = input("Nuevo cliente: ")
        producto = input("Nuevo producto: ")
        cantidad = int(input("Nueva cantidad: "))

        pedidos[indice]["cliente"] = cliente
        pedidos[indice]["producto"] = producto
        pedidos[indice]["cantidad"] = cantidad

        print("Pedido actualizado.")
    else:
        print("ID no válido.")

# FUNCIÓN: eliminar pedido
def eliminar_pedido():

    print("\n--- Eliminar Pedido ---")
    mostrar_pedidos()
    if len(pedidos) == 0:
        return
    indice = int(input("Ingrese el ID del pedido a eliminar: "))

    if indice >= 0 and indice < len(pedidos):
        pedidos.pop(indice)
        print("Pedido eliminado.")
    else:
        print("ID no válido.")

# MENÚ PRINCIPAL DEL SISTEMA

def menu():
    while True:

        print("\n====== SISTEMA DE GESTIÓN ======")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Registrar pedido")
        print("6. Mostrar pedidos")
        print("7. Editar pedido")
        print("8. Eliminar pedido")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_pedido()
        elif opcion == "6":
            mostrar_pedidos()
        elif opcion == "7":
            editar_pedido()
        elif opcion == "8":
            eliminar_pedido()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

# INICIO DEL PROGRAMA
menu()