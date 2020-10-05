from classes.persona import Persona
from controller.administrador_controller import Administrador_controller
from controller.almacen_controller import Almacen_controller
from controller.cajero_controller import Cajero_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Login_controller:
    def __init__(self):
        self.persona  = Persona()
        self.administrador_controller = Administrador_controller()
        self.almacen_controller = Almacen_controller()
        self.cajero_controller = Cajero_controller()
        self.salir = False
        


    def logeo(self):

        print('''
        =============
            Login
        =============
        ''')
        try:

            usuario = input_data("Ingrese su usuario >> ")
            password = input_data("Ingrese su password >> ")
            login = self.persona.buscar_personas({'usuario' : usuario, 'password': password })
            #print(print_table(login))
            if login:

                lista_persona = []
                for v in login:
                    id_persona  = v[0]
                    #id_empresa_rel = v[1]
                    #dni_persona = v[2]
                    nombres = v[3]
                    apellidos = v[4]
                    #correo = v[5]
                    #telefono = v[6]
                    #direccion = v[7]
                    id_tipo_rol = v[8]
                    usuario = v[9]
                    password = v[10]

                    usuario_login = self.persona.obtener_persona({
                        'id_persona': id_persona
                    })

                    lista_persona.append({
                        'id_persona' : usuario_login[0],
                        'id_empresa_rel' : usuario_login[1],
                        'dni_persona' : usuario_login[2],
                        'nombres' : usuario_login[3],
                        'apellidos' : usuario_login[4],
                        'correo' : usuario_login[5],
                        'telefono' : usuario_login[6],
                        'direccion' : usuario_login[7],
                        'id_tipo_rol': usuario_login[8],
                        'usuario' : usuario_login[9],
                        'password': usuario_login[10]
                    })
                    print(f'''
                    ==========================================================
                                Bienvenido : {nombres} {apellidos}
                    ==========================================================
                    ''')

                    if id_tipo_rol  == 1:
                        self.administrador_controller.menu()
                    elif id_tipo_rol  == 2:
                        self.almacen_controller.menu()
                    elif id_tipo_rol  == 3:
                        self.cajero_controller.menu()
                    else:
                        self.salir = True
                        break
            #print(lista_persona)
            
            #self.salir = True
            return lista_persona
        except Exception as e:
            print(f'{str(e)}')