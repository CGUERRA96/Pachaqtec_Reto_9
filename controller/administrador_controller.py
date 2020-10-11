from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from classes.venta import Venta
from classes.producto import Productos
from classes.venta_detalle import Venta_detalle
from classes.persona import Persona
from controller.persona_controller import Persona_controller

class Administrador_controller:
    def __init__(self):
        self.persona = Persona()
        self.producto = Productos()
        self.venta = Venta()
        self.venta_detalle = Venta_detalle()
        self.persona_controller = Persona_controller()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ==============================
                    Interfaz Administrador
                ==============================
                ''')
                menu = ['Mantenimiento Personal', 'Ver reporte de ventas', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.persona_controller.menu()
                elif respuesta == 2:
                    self.reporte_ventas()             
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
        print('''
        ========================
            Reporte de Ventas
        ========================
        ''')
        ventas_detalles = self.venta_detalle.obtener_ventas_detalles('id_venta_det')
        lista_ventas = []
        if ventas_detalles:
            for venta in ventas_detalles:
                buscar_venta = self.venta.obtener_venta({'id_venta': venta[1]})
                buscar_producto = self.producto.obtener_producto({'id_producto': venta[2]})
                cantidad = venta[3]
                monto_sin_igv = venta[4]
                igv = venta[5]
                precio_venta = precio_venta[6]
                lista_ventas.append((
                    venta[0],
                    buscar_venta[2],
                    buscar_producto[1],
                    cantidad,
                    monto_sin_igv,
                    igv,
                    precio_venta
                ))
        print(print_table(lista_ventas, ['ID', 'Doc. Comprador', 'Producto', 'Cantidad', 'Precio sin IGV', 'IGV', 'Precio Final']))
        input("\nPresione una tecla para continuar...")