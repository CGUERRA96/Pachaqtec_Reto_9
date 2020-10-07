from connection.conn import Conexion

class Empresa:
    def __init__(self):
        self.model = Conexion('empresa')

    def guardar_empresa(self, empresa):
        return self.model.insert(empresa)

    def obtener_empresa(self, id_empresa):
        return self.model.get_by_id(id_empresa)

    def obtener_empresas(self, order): #no se va ha usar pero lo dejo como parte del modelo
        return self.model.get_all(order)

    def buscar_empresas(self, data_empresa): #no se va ha usar pero lo dejo como parte del modelo
        return self.model.get_by_column(data_empresa)

    def modificar_empresa(self, id_empresa, data_empresa):
        return self.model.update(id_empresa, data_empresa)

    def eliminar_empresa(self, id_empresa):
        return self.model.delete(id_empresa)