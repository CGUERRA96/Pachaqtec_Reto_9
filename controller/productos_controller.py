from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from controller.categoria_controller import Categoria_controller
from classes.producto import Productos

class Productos_controller:
    def __init__(self):
        self.categoria_controller = Categoria_controller()
        self.producto = Productos()
        self.salir = False

    def menu(self):
         while True:
            try:
                print('''
                ============================
                    Almacen de Productos
                ============================
                ''')
                menu = [ 'Buscar productos', 'Ingresar productos', 'Mantenimiento Categoria Productos', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.buscar_productos()  
                elif respuesta == 2:
                    self.insertar_producto()
                elif respuesta == 3:
                    self.categoria_controller.menu()         
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
    
    def buscar_productos(self):
        print('''
        ========================
            Buscar Productos
        ========================
        ''')
        try:
            self.listar_productos()
            id_productos = input_data("Ingrese el ID del producto >> ", "int")
            productos = self.producto.obtener_producto({'id_productos': id_productos})
            #print(print_table(productos, ['id_productos', 'Nombre', 'id_categoria', 'fecha_ult_ingreso', 'vida_util', 'valor_unitario_compra', 'valor_unitario_venta', 'exonerado_igv', 'stock'])) #confirmar si debe ir categoria_producto (nombre de la tabla)

            if productos:
                if pregunta("¿Deseas dar mantenimiento a los productos?"):
                    opciones = ['Editar productos', 'Eliminar productos', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        if pregunta("Que deseas hacer?"):
                            opciones = ['Editar Campos', 'Actualzar Stock', 'Salir']
                            resp_edit = Menu(opciones).show()
                            if resp_edit == 1:
                                self.editar_productos(id_productos)
                            elif resp_edit == 2:
                                try:
                                    while True:
                                        stock = input_data("Ingrese la cantidad del producto en existencia >> ", "int")
                                        if stock >= productos[8]:
                                            self.producto.modificar_productos({
                                                'id_productos': id_productos
                                            }, {
                                                'nombre' : productos[1],
                                                'id_categoria' : productos[2],
                                                'fecha_ult_ingreso' : productos[3],
                                                'vida_util' :  productos[4],
                                                'valor_unitario_compra' : productos[5],
                                                'valor_unitario_venta' : productos[6], 
                                                'exonerado_igv' : productos[7],
                                                'stock': stock
                                            })
                                            print('''
                                            ==========================
                                                Producto Editado !
                                            ==========================
                                            ''')

                                            print(print_table(productos, ['id_productos', 'Nombre', 'id_categoria', 'fecha_ult_ingreso', 'vida_util', 'valor_unitario_compra', 'valor_unitario_venta', 'exonerado_igv', 'stock'])) #confirmar si debe ir categoria_producto (nombre de la tabla)
                                            break
                                        else:
                                            print('Por favor ingresar un numero mayor que el stock actual')

                                except ValueError as e:
                                    print(f'{str(e)}')

                    elif respuesta == 2:
                        self.eliminar_productos(id_productos)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")
    
    def insertar_producto(self):
        nombre = input_data("Ingrese el nombre del producto >> ")
        self.categoria_controller.listar_categorias()
        id_categoria = input_data("Ingrese el ID categoria del producto >> ", "int")
        fecha_ult_ingreso = input_data("Ingrese la fecha de ultimo ingreso del producto >> ")
        vida_util = input_data("Ingrese la vida util del producto en dias >> ", "int")
        valor_unitario_compra = input_data("Ingrese el valor unitario de compra del producto >> ", "float")
        valor_unitario_venta = input_data("Ingrese el valor unitario de venta del producto >> ", "float")
        exonerado_igv = input_data("Confirme si el producto se encuentra exonerado de igv (si o no) >> ")
        stock = input_data("Ingrese la cantidad del producto en existencia >> ", "int")
        self.producto.guardar_productos({
            'nombre': nombre,
            'id_categoria': id_categoria,
            'fecha_ult_ingreso': fecha_ult_ingreso,
            'vida_util': vida_util,
            'valor_unitario_compra': valor_unitario_compra,
            'valor_unitario_venta': valor_unitario_venta,
            'exonerado_igv': exonerado_igv,
            'stock': stock
                })
        print('''
        =================================
            Nuevo Producto agregado !
        =================================
        ''')
        self.listar_productos()
    
    def editar_productos(self, id_productos):
        nombre = input_data("Ingrese el nombre del producto >> ")
        self.categoria_controller.listar_categorias()
        id_categoria = input_data("Ingrese el ID categoria del producto >> ", "int")
        fecha_ult_ingreso = input_data("Ingrese la fecha de ultimo ingreso del producto >> ")
        vida_util = input_data("Ingrese la vida util del producto en dias >> ", "int")
        valor_unitario_compra = input_data("Ingrese el valor unitario de compra del producto >> ", "float")
        valor_unitario_venta = input_data("Ingrese el valor unitario de venta del producto >> ", "float")
        exonerado_igv = input_data("Confirme si el producto se encuentra exonerado de igv (si o no) >> ")
        stock = input_data("Ingrese la cantidad del producto en existencia >> ", "int")
        self.producto.modificar_productos({
            'id_productos': id_productos
        }, {
            'nombre': nombre,
            'id_categoria': id_categoria,
            'fecha_ult_ingreso': fecha_ult_ingreso,
            'vida_util': vida_util,
            'valor_unitario_compra': valor_unitario_compra,
            'valor_unitario_venta': valor_unitario_venta,
            'exonerado_igv': exonerado_igv,
            'stock': stock
        })
        print('''
        ==========================
            Producto Editado !
        ==========================
        ''')
    
    def eliminar_productos(self, id_productos):
        self.producto.eliminar_productos({
            'id_productos': id_productos
        })
        print('''
        =============================
            Producto Eliminado !
        =============================
        ''')