# Importamos las clases necesarias desde el paquete de modelos
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase de servicio que administra el catálogo de productos y registros de clientes."""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        # Uso de listas como tipo de dato compuesto para almacenar múltiples objetos
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def registrar_producto(self, nuevo_producto: Producto) -> None:
        """Agrega un objeto de tipo Producto al catálogo."""
        self.lista_productos.append(nuevo_producto)

    def registrar_cliente(self, nuevo_cliente: Cliente) -> None:
        """Agrega un objeto de tipo Cliente al registro."""
        self.lista_clientes.append(nuevo_cliente)

    def mostrar_inventario_productos(self) -> None:
        """Muestra en consola de forma organizada todos los productos registrados."""
        print(f"\n--- MENÚ DE PRODUCTOS: {self.nombre_restaurante.upper()} ---")
        if not self.lista_productos:
            print("No hay productos registrados en el menú.")
        for producto in self.lista_productos:
            print(producto)  # Invoca automáticamente al método __str__ de Producto

    def mostrar_registro_clientes(self) -> None:
        """Muestra en consola de forma organizada todos los clientes registrados."""
        print(f"\n--- REGISTRO DE CLIENTES ASOCIADOS ---")
        if not self.lista_clientes:
            print("No hay clientes registrados en el sistema.")
        for cliente in self.lista_clientes:
            print(cliente)  # Invoca automáticamente al método __str__ de Cliente