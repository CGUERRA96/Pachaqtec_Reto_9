from connection.conn import Conexion

class Tipo_Rol:
    def __init__(self):
        self.model = Conexion('tipo_rol')

    def guardar_tipo_rol(self, tipo_rol):
        return self.model.insert(tipo_rol)

    def obtener_tipo_roles(self, order):
        return self.model.get_all(order)