from Datos.Conexion import Conexion
from Modelo.Usuario import Usuario
import pyodbc

class UsuarioDAO():
    db=None

    def __init__(self):
        cn=Conexion()
        self.db=cn.getDB()

    def validar(self, nombreUsuario, Contrasenia):
        sql="Select idUsuario, nombre, contra, estatus, tipo, fechaRegistro from Usuarios where nombre=%s" \
            "and contra=%s"

        try:
            cursor = self.db.cursor()
            cursor.execute(sql, (nombreUsuario, Contrasenia))
            rs=cursor.fetchone()
            u={"id":rs[0], "nombre":rs[1], "contra":rs[2], "estatus":rs[3],
               "tipo":rs[4], "fechaRegistro":rs[5]}

            cursor.close()
            self.db.close()
        except(ValueError):
            print('Error al ejecutar la Base de Datos '+ ValueError)
        return u


