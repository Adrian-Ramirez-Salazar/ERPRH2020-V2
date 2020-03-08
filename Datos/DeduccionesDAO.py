import pyodbc

from Datos.Conexion import Conexion
from Modelo.Deducciones import Deducciones

class DeduccionesDAO:
    db = None

    def __init__(self):
        cn = Conexion()
        self.db = cn.getDB()

    def consultaGeneral(self):
        sql = "SELECT *FROM RH.Deducciones WHERE idDeduccion!=0;"
        lista = []
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            rs = cursor.fetchall()
            for reg in rs:
                d = Deducciones(reg[0], reg[1], reg[2], reg[3])
                lista.append(d)
            cursor.close()
            self.db.close()
        except:
            print('Error al ejecutar la consola')
        return lista