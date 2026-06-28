# Punto de arranque de la aplicación modular
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente

def ejecutar_sistema() -> None:
    # 1. Instanciar el servicio principal del restaurante
    mi_restaurante = Restaurante("Sabores de Mi Tierra")

    # 2. Crear al menos dos objetos de cada modelo
    # Creación de Productos
    plato_principal = Producto("Asado de Tira con Papas", 14.50, 25, True)
    bebida_refrescante = Producto("Jugo Natural de Maracuyá", 2.75, 5, True)
    postre_especial = Producto("Volcán de Chocolate", 5.00, 15, False) # No disponible temporalmente

    # Creación de Clientes
    cliente_uno = Cliente("1723456789", "Carlos Javier Mendoza", 12, True)
    cliente_dos = Cliente("0918273645", "María Elena Espinoza", 2, False)

    # 3. Agregar los objetos creados a las listas administradas por el servicio principal
    mi_restaurante.registrar_producto(plato_principal)
    mi_restaurante.registrar_producto(bebida_refrescante)
    mi_restaurante.registrar_producto(postre_especial)

    mi_restaurante.registrar_cliente(cliente_uno)
    mi_restaurante.registrar_cliente(cliente_dos)

    # 4. Mostrar la información registrada de forma organizada en consola
    mi_restaurante.mostrar_inventario_productos()
    mi_restaurante.mostrar_registro_clientes()

if __name__ == "__main__":
    ejecutar_sistema()