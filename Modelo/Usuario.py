class Usuario:
    id=None
    nombre=None
    contra=None
    estatus=None
    tipo=None
    fechaRegistro=None

    def setId(self, id):
        self.id=id
    def getId(self):
        return self.id

    def setnombre(self, nombre):
        self.nombre=nombre
    def getnombre(self):
        return self.nombre

    def setcontra(self, contra):
        self.contra=contra
    def getcontra(self):
        return self.contra

    def setestatus(self, estatus):
        self.estatus=estatus
    def getestatus(self):
        return self.estatus

    def settipo(self, tipo):
        self.tipo=tipo
    def gettipo(self):
        return self.tipo

    def setfechaRegistro(self, fechaRegistro):
        self.fechaRegistro=fechaRegistro
    def getfechaRegistro(self):
        return self.fechaRegistro