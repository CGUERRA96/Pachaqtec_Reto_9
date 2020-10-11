from classes.persona import Persona
from controller.productos_controller import Productos_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Cajero_controller:
    def __init__(self):
        self.persona = Persona()
        self.productos_controller = Productos_controller()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ==============================
                    Interfaz Cajero
                ==============================
                ''')
                menu = ['Ingresar productos', 'Mantenimiento productos', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.productos_controller.listar_productos()
                elif respuesta == 2:
                    self.productos_controller.listar_venta_detalle_agrupador()                
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')