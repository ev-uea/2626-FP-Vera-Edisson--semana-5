class Producto:
    """Clase que representa un plato, bebida o artículo del restaurante."""

    def __init__(self, nombre: str, precio: float, tiempo_preparacion_minutos: int, disponible: bool):
        # Aplicamos identificadores descriptivos y tipos de datos básicos sugeridos
        self.nombre: str = nombre
        self.precio: float = precio
        self.tiempo_preparacion_minutos: int = tiempo_preparacion_minutos
        self.disponible: bool = disponible

    def __str__(self) -> str:
        # Método especial para representar el objeto como texto
        estado: str = "Disponible" if self.disponible else "Agotado"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Tiempo: {self.tiempo_preparacion_minutos} min | Estado: {estado}"