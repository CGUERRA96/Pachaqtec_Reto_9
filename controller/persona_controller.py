from classes.persona import Persona
from classes.empresa import Empresa
from classes.tipo_rol import Tipo_Rol
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Persona_controller:
    def __init__(self):
        self.persona = Persona()
        self.empresa = Empresa()
        self.tipo_rol = Tipo_Rol()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ==============================
                    Mantenimiento Personas
                ==============================
                ''')
                menu = ['Listar Personas', 'Registrar Persona', 'Buscar Personas', "Salir"]
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

    def listar_personas(self):
        print('''
        =======================
        =  Lista de Personas  =
        =======================
        ''')
        #personas_adm = self.persona.obtener_personas('id_persona')
        persona = self.persona.obtener_personas('id_persona')
        print(print_table(persona, ['ID', 'ID Empresa', 'DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono', 'Direccion', 'id_tipo_rol', 'Usuario','Password']))
        input("\nPresione una tecla para continuar...")

    def listar_administradores(self):
        #Buscar administradores (filtro administrador rol)
        print('''
        ==============================
        =  Lista de Administradores  =
        ==============================
        ''')
        id_tipo_rol = 1
        persona = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        print(print_table(persona, ['ID', 'ID Empresa', 'DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono', 'Direccion', 'id_tipo_rol', 'Usuario','Password']))
        input("\nPresione una tecla para continuar...")

    def listar_almacenero(self):
        #Buscar lectores (filtro lector rol)
        print('''
        =======================
        =  Lista de Lectores  =
        =======================
        ''')
        id_tipo_rol = 2
        persona = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        print(print_table(persona, ['ID', 'ID Empresa', 'DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono', 'Direccion', 'id_tipo_rol', 'Usuario','Password']))
        input("\nPresione una tecla para continuar...")

    def listar_cajeros(self):
        #Buscar lectores (filtro lector rol)
        print('''
        =======================
        =  Lista de Lectores  =
        =======================
        ''')
        id_tipo_rol = 3
        persona = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        print(print_table(persona, ['ID', 'ID Empresa', 'DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono', 'Direccion', 'id_tipo_rol', 'Usuario','Password']))
        input("\nPresione una tecla para continuar...")

    def inscribir_personas(self):
        #Ingresa persona y coloca su rol (1: Administrador y 2: Lector)
        id_empresa_rel = input_data("Ingrese el ID empresa >> ", "int")
        dni = input_data("Ingrese el nuevo DNI >> ")
        nombre = input_data("Ingrese el nuevo nombre >> ")
        apellidos = input_data("Ingrese el nuevo apellido >> ")
        correo = input_data("Ingrese el nuevo correo >> ")
        telefono = input_data("Ingrese el nuevo telefono >> ")
        direccion = input_data("Ingrese la nueva direccion >> ")
        id_tipo_rol = input_data("Ingrese el ID rol >> ", "int")
        usuario = input_data("Ingrese un usuario >> ")
        password = input_data("Ingresar un password >> ")
        self.persona.guardar_persona({
            'id_empresa_rel' : id_empresa_rel,
            'dni_persona ': dni,
            'nombres': nombre,
            'apellidos': apellidos,
            'correo': correo,
            'telefono': telefono,
            'direccion': direccion,
            'id_tipo_rol': id_tipo_rol,
            'usuario' : usuario,
            'password' : password 
        })
        print('''
        ==========================
            Persona Agregada !
        ==========================
        ''')

        self.listar_personas()


    # Ingreso de usuario admin


    def registro_maestro(self):
        #Ingresa persona y coloca su rol (1: Administrador y 2: Lector)
        
        empresa = self.empresa.obtener_empresas('id_empresa')
        if not empresa:
            list_empresa = []
            #for v in empresa:
            #    id_empresa = v[0],
            #    ruc = v[1],
            #    nombre_empresa = v[2],
            #    direccion = v[3]
            #
            list_empresa.append({
                'ruc' : 101010,
                'nombre_empresa' : 'Market S.A.',
                'direccion' : 'Lima'
            })
            #print(list_empresa[0]['ruc'])
            #    
            #list_empresa[1] = 101010101010,
            #list_empresa[2] = 'Market S.A.',
            #list_empresa[3] = 'Lima'
            self.empresa.guardar_empresa({
                'ruc' : int(list_empresa[0]['ruc']),
                'nombre_empresa' : list_empresa[0]['nombre_empresa'],
                'direccion' : list_empresa[0]['direccion']
            })
        
        id_empresa_rel = 1
        dni = '999999'
        nombre = 'admin'
        apellidos = 'admin'
        correo = 'admin@gmail.com'
        telefono = '999999'
        direccion = 'admin'

        tipo_rol = self.tipo_rol.obtener_tipo_roles('id_tipo_rol')
        if not tipo_rol:
            list_tipo_rol = []

            list_tipo_rol.append({
                'tipo_rol' : 'Administrador'
            })

            #tipo_rol = 'Administrador'
            self.tipo_rol.guardar_tipo_rol({
                'tipo_rol' : list_tipo_rol[0]['tipo_rol']
            })

        id_tipo_rol = 1
        usuario = 'admin'
        password = 'admin'
        self.persona.guardar_persona({
            'id_empresa_rel' : id_empresa_rel,
            'dni_persona ': dni,
            'nombres': nombre,
            'apellidos': apellidos,
            'correo': correo,
            'telefono': telefono,
            'direccion': direccion,
            'id_tipo_rol': id_tipo_rol,
            'usuario' : usuario,
            'password' : password 
        })

