from Datos.Conexion import Conexion
from Modelo.Estado import Estado

class EstadoDAO:
    db=None
    def __init__(self):
        cn=Conexion()
        self.db=cn.getDB()

    def consultarNombre(self):
        sql='Select idEstado, nombre, siglas from RH.Estado;'
        lista=[]

        try:
            cursor=self.db.cursor()
            cursor.execute(sql)
            rs=cursor.fetchall()
            for reg in rs:
                e=Estado(reg[0], reg[1], reg[2])
                lista.append(e)
            cursor.close()
            self.db.close()
        except:
            print('Error al ejecutar la consola')
        return lista