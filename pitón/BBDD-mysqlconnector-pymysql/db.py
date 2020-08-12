# Agenda con base de datos Sqlite3
import pymysql

def create_db():
    '''Creación de la Base de datos'''

    conexion = pymysql.connect(host='localhost', #127.0.0.1
                                user='root',      #admin o cualquier otro usuario
                                password='',
                                db='test')
    consulta = conexion.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS contactos(id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre VARCHAR(20) NOT NULL, apellidos VARCHAR(20) NOT NULL, telefono VARCHAR(14) NOT NULL, email VARCHAR(20) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla: ", e)
    conexion.close()


def connect():
    '''Conexión a la Base de datos'''

    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='agenda')
        print("Conexión correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)


def insert_data(nombre, apellidos, telefono, email):
    '''Agregar datos en la Base de Datos'''

    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='agenda')

    consulta = conexion.cursor()

    datos = (nombre, apellidos, telefono, email)
    sql = 'INSERT INTO contactos(nombre,apellidos,telefono,email) VALUES (?,?,?,?)'

    try:
        consulta.execute(sql, datos)
        print("Datos guardados con exito")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al intentar guardar los datos: ", e)
    conexion.commit()
    conexion.close()


def update_data(id, nombre, apellidos, telefono, email):
    '''Actualizar datos en la Base de Datos'''
    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='agenda')
    consulta = conexion.cursor()
    consulta.execute('UPDATE agenda SET nombre = ?,apellidos = ?,telefono = ?,email = ? WHERE id= ?', (nombre, apellidos, telefono, email, str(id)))
    consulta.close()
    conexion.commit()
    conexion.close()


def get_data():
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='test')

        sql_select_Query = "select * from agenda"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
           if row=='':
               print("No hay contactos...")
           else:
               print('[+]Nombre:',row[0],'\n[+]Telefono:',row[1],'\n[+]E-Mail:',row[2],"\n----------")  #Mostramos La lista)

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
