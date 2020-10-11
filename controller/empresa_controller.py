from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from classes.empresa import Empresa

class Empresa_controller:
    def __init__(self):
        self.empresa = Empresa()
        self.salir = False
    
    def menu(self):
        while True:
            try:
                print('''
                ================================
                    Datos de su empresa
                ================================
                ''')
                menu = ['Ver datos de la empresa', "Ingresar datos de la empresa", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_empresa()
                elif respuesta == 2:
                    self.insertar_empresa()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_empresa(self):
        print('''
        ===========================
            Lista de Empresas
        ===========================
        ''')

        empresa = self.empresa.obtener_empresas('id_empresa')
        print(print_table(empresa,['ID', 'RUC', 'Nombre', 'Dirección']))

    def buscar_empresa(self):
        print('''
        ===========================
            Datos de la Empresa
        ===========================
        ''')
        try:
            id_empresa = 1
            empresa = self.empresa.obtener_empresa({'id_salon': id_empresa})
            print(print_table(empresa, ['ID', 'RUC', 'Nombre', 'Dirección']))

            if empresa:
                if pregunta("¿Deseas dar mantenimiento a los datos de su empresa?"):
                    opciones = ['Editar datos', 'Eliminar datos', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_empresa(id_empresa)
                    elif respuesta == 2:
                        self.eliminar_empresa(id_empresa)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_empresa(self):
        ruc = input_data("Ingrese RUC de su empresa >> ")
        nombre = input_data("Ingrese el nombre de su empresa >> ")
        direccion = input_data("Ingrese la dirección de su empresa >> ")
        self.empresa.guardar_empresa({
            'ruc': ruc,
            'nombre_empresa': nombre,
            'direccion': direccion
        })
        print('''
        =========================================
            Datos de su empresa registrados !
        =========================================
        ''')
        self.listar_empresa()

    def editar_empresa(self, id_empresa):
        ruc = input_data("Ingrese el nuevo RUC de su empresa >> ")
        nombre = input_data("Ingrese el nuevo nombre de su empresa >> ")
        direccion = input_data("Ingrese la nueva dirección de su empresa >> ")
        self.empresa.modificar_empresa({
            'id_empresa': id_empresa
        }, {
            'ruc': ruc,
            'nombre_empresa': nombre,
            'direccion': direccion
        })
        print('''
        ==================================
            Datos de Empresa Editado !
        ==================================
        ''')

    def eliminar_empresa(self, id_empresa):
        self.empresa.eliminar_empresa({
            'id_empresa': id_empresa
        })
        print('''
        ========================
            Datos Eliminados !
        ========================
        ''')