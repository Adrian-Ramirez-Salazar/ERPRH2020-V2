from pyodbc import connect
class Conexion:
    db=None

    def __init__(self):
        self.db=connect('Driver={SQL Server}; '
                               'Server=DESKTOP-8SKO2G9\SQLEXPRESS;'
                               ' Database=ERP2020;')

    def getDB(self):
        return self.db

    def cerrar(self):
        self.db.close()


    def consultarFoto(self, id):
        sql = "Select fotografia from RH.Empleados where idEmpleado=?"
        db=self.getDB()
        if(db!='false'):
            cursor=db.cursor()
            cursor.execute(sql,(id,))
            rs=cursor.fetchone()
            cursor.close()
            db.close()
            return rs[0]