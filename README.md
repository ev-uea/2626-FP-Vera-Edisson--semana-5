# Sistema Básico de Gestión de Restaurante (`restaurante_app`)

**Estudiante:** Edisson Valentin Vera Gamboa  
**Asignatura:** Programación Orientada a Objetos   
**Semana:** 5 - Organización modular de un sistema orientado a objetos en Python  
**Paralelo:** E
---

## 1. Descripción del Sistema
Este proyecto consiste en un sistema básico para la gestión interna de un restaurante desarrollado bajo el paradigma de la Programación Orientada a Objetos. El software permite modelar de forma estructurada productos alimenticios y clientes frecuentes, centralizando su manipulación a través de una clase de servicio que actúa como el núcleo administrativo del negocio. El programa se ejecuta de manera modular, demostrando el flujo de datos e importaciones sin necesidad de menús interactivos complejos ni interfaces gráficas.

---

## 2. Estructura del Proyecto
El proyecto está organizado de manera modular respetando la separación de responsabilidades en las siguientes carpetas y archivos:

```text
restaurante_app/
├── modelos/                  
│   ├── __init__.py          
│   ├── producto.py          
│   └── cliente.py             
├── servicios/                
│   ├── __init__.py           
│   └── restaurante.py        
└── main.py                   