from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_persona(self):        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  personas(
                id_persona  SERIAL PRIMARY KEY NOT NULL,
                id_empresa_rel bigint NOT NULL,
                dni_persona varchar(8) NOT NULL,
                nombres varchar(100) NOT NULL,
                apellidos varchar(50) NOT NULL,
                correo varchar(60) NOT NULL,
                telefono varchar(20) NOT NULL,
                direccion varchar(20) NOT NULL,
                id_tipo_rol int NOT NULL,
                usuario varchar(150) NOT NULL,
                password varchar(200) NOT NULL,
                CONSTRAINT FK_TipoRol FOREIGN KEY (id_tipo_rol) REFERENCES tipo_rol(id_tipo_rol),
                CONSTRAINT FK_Empresa FOREIGN KEY (id_empresa_rel) REFERENCES empresa(id_empresa)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_tipo_rol(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  tipo_rol(
                id_tipo_rol  SERIAL  PRIMARY KEY NOT NULL,
                tipo_rol varchar(25) NOT NULL                              
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
    
    def crear_empresa(self):        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  empresa(
                id_empresa  SERIAL PRIMARY KEY NOT NULL,
                ruc int NOT NULL,
                nombre_empresa varchar(150) NOT NULL,
                direccion varchar(150) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_categoria_producto(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  categoria_producto(
                id_categoria  SERIAL  PRIMARY KEY NOT NULL,
                descripcion varchar(100) NOT NULL                
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
                
    def crear_productos(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  productos(
                id_productos  SERIAL  PRIMARY KEY NOT NULL,
                nombre varchar(100) NOT NULL,
                id_categoria integer NOT NULL,
                fecha_ult_ingreso date NOT NULL,
                vida_util int NOT NULL,
                valor_unitario_compra real NOT NULL,
                valor_unitario_venta real NOT NULL,
                exonerado_igv varchar(2) NOT NULL,
                stock int NOT NULL,
                FOREIGN KEY (id_categoria) REFERENCES categoria_producto(id_categoria) 
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_venta(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  venta(
                id_venta SERIAL  PRIMARY KEY NOT NULL,
                tipo_documento_comprador int NOT NULL,
                documento_comprador int NOT NULL,
                direccion_comprador varchar(150) NOT NULL,
                tipo_comprobante integer,
                fecha_prestamo timestamp NOT NULL,
                id_cajero int NOT NULL,
                CONSTRAINT FK_cajero FOREIGN KEY (id_cajero) REFERENCES personas(id_persona)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_venta_detalle(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  venta_detalle(
                id_venta_det SERIAL PRIMARY KEY NOT NULL,
                id_venta int  NOT NULL,
                id_producto int NOT NULL ,
                cantidad int NOT NULL,
                monto_sin_igv real NOT NULL,
                igv real NOT NULL,
                precio_venta real NOT NULL,
                CONSTRAINT FK_venta FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
                CONSTRAINT FK_producto FOREIGN KEY (id_producto) REFERENCES productos(id_productos)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
                
    

conn = Conexion('sistema_market')
db= Database(conn)
db.crear_tipo_rol()
db.crear_empresa()
db.crear_persona()
db.crear_categoria_producto()
db.crear_productos()
db.crear_venta()
db.crear_venta_detalle()
conn.close_connection()
