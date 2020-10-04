from connection.conn import Conexion

class Venta_detalle:
    def __init__(self):
        self.model = Conexion('venta_detalle')

    def guardar_venta_detalle(self, venta_detalle):
        return self.model.insert(venta_detalle)

    def obtener_venta_detalle(self, id_venta_detalle):
        return self.model.get_by_id(id_venta_detalle)

    def obtener_ventas_detalles(self, order):
        return self.model.get_all(order)

    def buscar_ventas_detalles(self, data_venta_detalle):
        return self.model.get_by_column(data_venta_detalle)

    def modificar_ventas_detalles(self, id_venta_detalle, data_venta_detalle):
        return self.model.update(id_venta_detalle, data_venta_detalle)

    def eliminar_ventas_detalles(self, id_venta_detalle):
        return self.model.delete(id_venta_detalle)