from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from classes.venta import Venta
from classes.producto import Producto
from classes.venta_detalle import Venta_detalle
from classes.persona import Persona

class Administrador_controller:
    def __init__(self):
        self.persona = Persona()
        self.producto = Producto()
        self.venta = Venta()
        self.venta_detalle = Venta_detalle()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ==============================
                    Interfaz Administrador
                ==============================
                ''')
                menu = ['Ver productos en almacen', 'Ver reporte de ventas', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_productos()
                elif respuesta == 2:
                    pass                
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

        def listar_productos(self):
            print('''
            ==========================
                Lista de Productos
            ==========================
            ''')
            productos = self.producto.obtener_productos('id_productos')
            print(print_table(productos, ['ID', 'Nombre Producto', 'ID Categoria', 'Fecha Ingreso', 'Vida Util', 'Valor Unitario Compra', 'Valor Unitario Venta', 'Exogeración', 'Stock']))
            input("\nPresione una tecla para continuar...")

        def reporte_ventas(self):
            pass