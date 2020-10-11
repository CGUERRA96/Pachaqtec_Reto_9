from classes.persona import Persona
from classes.empresa import Empresa
from classes.tipo_rol import Tipo_rol
from controller.empresa_controller import Empresa_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Persona_controller:
    def __init__(self):
        self.persona = Persona()
        self.empresa = Empresa()
        self.tipo_rol = Tipo_rol()
        self.empresa_controller =  Empresa_controller()
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
                    self.listar_personas()
                elif respuesta == 2:
                    self.inscribir_personas()
                elif respuesta == 3:
                    pass
                    #self.buscar_personas()  
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
        #print(print_table(persona, ['ID', 'ID Empresa', 'DNI', 'Nombre', 'Apellidos', 'Email', 'Telefono', 'Direccion', 'id_tipo_rol', 'Usuario','Password']))
        #input("\nPresione una tecla para continuar...")
        
        view_persona = []

        for p in persona:
            id_persona = p[0]
            id_empresa_rel = p[1]
            dni  = p[2]
            nombre  = p[3]
            apellidos = p[4]
            correo = p[5]
            telefono = p[6]
            direccion = p[7]
            id_tipo_rol_rel = p[8]
            usuario = p[9]
            password  = p[10]

            view_empresa = []
            empresa = self.empresa.obtener_empresas('id_empresa')
            for e in empresa:
                id_empresa = e[0]
                ruc = e[1]
                nombre_empresa = e[2]
                direccion = e[3]

                if id_empresa_rel == id_empresa:
                    nombre_empresa = nombre_empresa

                view_empresa.append({
                    'id_empresa' : id_empresa,
                    'ruc' : ruc,
                    'nombre_empresa' : nombre_empresa,
                    'direccion' : direccion
                })
                
                view_tipo_rol = []
                tipo_rol = self.tipo_rol.obtener_tipo_roles('id_tipo_rol')
                for t in tipo_rol:
                    id_tipo_rol = t[0]
                    tipo_rol = t[1]

                    if id_tipo_rol_rel == id_tipo_rol:
                        descripcion = tipo_rol

                    view_tipo_rol.append({
                    'id_tipo_rol' : id_tipo_rol,
                    'tipo_rol' : tipo_rol
                    })

            view_persona.append({
                'id_persona' : id_persona,
                'nombre_empresa' : nombre_empresa,
                'dni'  : dni,
                'nombre'  : nombre,
                'apellidos' : apellidos,
                'correo' : correo,
                'telefono' : telefono,
                'direccion' : direccion,
                'tipo_rol' : descripcion,
                'usuario' : usuario,
                'password'  : password
            })
        print(print_table(view_persona))

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
        self.empresa_controller.listar_empresa()
        id_empresa_rel = input_data("Ingrese el ID empresa >> ", "int")
        dni = input_data("Ingrese el nuevo DNI >> ")
        nombre = input_data("Ingrese el nuevo nombre >> ")
        apellidos = input_data("Ingrese el nuevo apellido >> ")
        correo = input_data("Ingrese el nuevo correo >> ")
        telefono = input_data("Ingrese el nuevo telefono >> ")
        direccion = input_data("Ingrese la nueva direccion >> ")
        roles = self.tipo_rol.obtener_tipo_roles('id_tipo_rol')
        print(print_table(roles,['ID', 'Tipo Rol1']))
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

            list_empresa.append({
                'ruc' : 101010,
                'nombre_empresa' : 'Market S.A.',
                'direccion' : 'Lima'
            })

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

