from connection.conn import Conexion

class Empresa:
    def __init__(self):
        self.model = Conexion('empresa')

    def guardar_empresa(self, empresa):
        return self.model.insert(empresa)

    def obtener_empresas(self, order):
        return self.model.get_all(order)