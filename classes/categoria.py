from connection.conn import Conexion

class Categoria:
    def __init__(self):
        self.model = Conexion('categoria_producto')

    def guardar_categorias_producto(self, categorias_producto):
        return self.model.insert(categorias_producto)

    def obtener_categorias_producto(self, id_categoria):
        return self.model.get_by_id(id_categoria)

    def obtener_categorias_productos(self, order):
        return self.model.get_all(order)

    def buscar_categorias_producto(self, data_categoria_producto):
        return self.model.get_by_column(data_categoria_producto)

    def modificar_categorias_producto(self, id_categoria, data_categoria_producto):
        return self.model.update(id_categoria, data_categoria_producto)

    def eliminar_categorias_producto(self, id_categoria):
        return self.model.delete(id_categoria)