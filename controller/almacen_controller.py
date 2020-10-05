from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from controller.productos_controller import Productos_controller

class Almacen_controller:
    def __init__(self):
        self.productos_controller = Productos_controller()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ============================
                    Almacen de Productos
                ============================
                ''')
                menu = ['Ingresar productos', 'Mantenimiento productos', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.productos_controller.insertar_producto()
                elif respuesta == 2:
                    self.productos_controller.buscar_productos()                
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    