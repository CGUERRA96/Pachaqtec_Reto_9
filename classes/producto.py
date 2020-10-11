from connection.conn import Conexion

class Productos:
    def __init__(self):
        self.model = Conexion('productos')

    def guardar_productos(self, productos):
        return self.model.insert(productos)

    def obtener_producto(self, id_productos):
        return self.model.get_by_id(id_productos)

    def obtener_productos(self, order):
        return self.model.get_all(order)

    def buscar_productos(self, data_productos):
        return self.model.get_by_column_like(data_productos)

    def modificar_productos(self, id_productos, data_productos):
        return self.model.update(id_productos, data_productos)

    def eliminar_productos(self, id_productos):
        return self.model.delete(id_productos)