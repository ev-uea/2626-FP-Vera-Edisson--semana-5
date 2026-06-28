class Cliente:
    """Clase que representa a un cliente registrado en el restaurante."""

    def __init__(self, cedula: str, nombre_completo: str, visitas_realizadas: int, es_cliente_frecuente: bool):
        # Atributos explícitos usando str, int y bool
        self.cedula: str = cedula
        self.nombre_completo: str = nombre_completo
        self.visitas_realizadas: int = visitas_realizadas
        self.es_cliente_frecuente: bool = es_cliente_frecuente

    def __str__(self) -> str:
        # Método especial para representar el cliente como texto
        tipo_cliente: str = "Frecuente (Aplica Descuento)" if self.es_cliente_frecuente else "Regular"
        return f"Cliente: {self.nombre_completo} (ID: {self.cedula}) | Visitas: {self.visitas_realizadas} | Tipo: {tipo_cliente}"