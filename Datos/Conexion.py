import pyodbc
class Conexion:
    db=None

    def __init__(self):
        self.db=pyodbc.connect(Driver="{SQL Server};", Server="DESKTOP-8SKO2G9\SQLEXPRESS;", db='ERP2020;', Trusted_Connection='yes;')

    def getDB(self):
        return self.db

    def cerrar(self):
        self.db.close()
