from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from classes.categoria import Categoria

class Categoria_controller:
    def __init__(self):
        self.categorias = Categoria()
        self.salir = False
    
    def menu(self):
        while True:
            try:
                print('''
                ================================
                    Categorias por Productos
                ================================
                ''')
                menu = ['Listar categorias', 'Buscar categorias', "Nueva categoria", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_categorias()
                elif respuesta == 2:
                    self.buscar_categorias()
                elif respuesta == 3:
                    self.insertar_categorias()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')
    
    def listar_categorias(self):
        print('''
        ===========================
            Lista de Categorias
        ===========================
        ''')
        categorias = self.categorias.obtener_categorias_productos('id_categoria')
        print(print_table(categorias, ['id_categoria', 'descripcion']))
        input("\nPresione una tecla para continuar...")
    
    def buscar_categorias(self):
        print('''
        =========================
            Buscar Categorias
        =========================
        ''')
        try:
            id_categoria = input_data("Ingrese el ID de la categoria >> ", "int")
            categorias = self.categorias.obtener_categorias_producto({'id_categoria': id_categoria})
            print(print_table(categorias, ['id_categoria', 'descripcion']))

            if categorias:
                if pregunta("¿Deseas dar mantenimiento a las categorias?"):
                    opciones = ['Editar categorias', 'Eliminar categorias', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_categorias(id_categoria)
                    elif respuesta == 2:
                        self.eliminar_categorias(id_categoria)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    
    def insertar_categorias(self):
        nombre = input_data("Ingrese el nombre de la categoria >> ")        
        self.categorias.guardar_categorias_producto({
            'descripcion': nombre,
                })
        print('''
        ==================================
            Nueva Categoria agregada !
        ==================================
        ''')
        self.listar_categorias()
    
    def editar_categorias(self, id_categoria):
        nombre = input_data("Ingrese el nuevo nombre de la categoria >> ")
        self.categorias.modificar_categorias_producto({
            'id_categoria': id_categoria
        }, {
            'descripcion': nombre,
        })
        print('''
        ===========================
            Categoria Editada !
        ===========================
        ''')
    
    def eliminar_categorias(self, id_categoria):
        self.categorias.eliminar_categorias_producto({
            'id_categoria': id_categoria
        })
        print('''
        =============================
            Categoria Eliminada !
        =============================
        ''')