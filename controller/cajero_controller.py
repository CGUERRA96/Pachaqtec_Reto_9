from classes.persona import Persona
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Cajero_controller:
    def __init__(self):
        self.persona = Persona()
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
                    pass
                elif respuesta == 2:
                    pass                
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')