from classes.persona import Persona
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Login_controller:
    def __init__(self):
        self.persona  = Persona()
        
    def menu(self):
        while True:
            try:
                print('''
                =============================
                   Mantenimiento de Libros
                =============================
                ''')
                menu = ['Login', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.logeo()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def logeo(self):

        print('''
        =============
            Login
        =============
        ''')
        try:

            usuario = input_data("Ingrese su usuario >> ")
            password = input_data("Ingrese su usuario >> ")
            login = self.persona.buscar_personas({'usuario' : usuario, 'password': password })
            print(print_table(login))

            #if libros:
            #    if pregunta(f"¿Deseas dar mantenimiento al libro?"):
            #        opciones = ['Editar libro', 'Salir']
            #        respuesta = Menu(opciones).show()
            #        if respuesta == 1:
            #            self.editar_libro(id_libro)
        except Exception as e:
            print(f'{str(e)}')