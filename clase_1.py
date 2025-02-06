class Carrito:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto: dict):
        self.productos.append(producto)
        self.total += producto['precio']

    def agregar_productos_lista(self, productos: list):
        for producto in productos:
            self.agregar_producto(producto)

    def eliminar_producto(self, nombre_producto: str):
        for producto in self.productos:
            if producto['nombre'] == nombre_producto:
                self.total -= producto['precio']
                self.productos.remove(producto)
                break

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Descripción: {producto['descripcion']}")

    def obtener_total(self):
        return self.total

def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Mostrar total")
    print("5. Salir")

def main():
    mi_carrito = Carrito('Mi carrito')

    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            descripcion = input("Descripción del producto: ")
            producto = {'nombre': nombre, 'precio': precio, 'descripcion': descripcion}
            mi_carrito.agregar_producto(producto)
            print(f"Producto '{nombre}' agregado.")
        elif opcion == 2:
            nombre = input("Nombre del producto a eliminar: ")
            mi_carrito.eliminar_producto(nombre)
            print(f"Producto '{nombre}' eliminado.")
        elif opcion == 3:
            print("Productos en el carrito:")
            mi_carrito.mostrar_productos()
        elif opcion == 4:
            print(f"Total: {mi_carrito.obtener_total()}")
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
