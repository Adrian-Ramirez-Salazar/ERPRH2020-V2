from flask import Flask, render_template, request, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from werkzeug.utils import redirect

from Datos.usuarioDAO import UsuarioDAO


app = Flask(__name__)
app.secret_key=b'yangars'


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8SKO2G9\SQLEXPRESS;'
                      'Database=ERP2020;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()




#Nos direcciona a la pagina para logearse
@app.route('/')
def index():
    return render_template('Login.html')




#Direcciona a la pagina principal del sistema
@app.route('/login', methods=['GET','POST'])
def login():
    try:
        server = 'localhost'
        database = 'ERP2020'
        username = request.form['Usuario']
        password = request.form['Contraseña']
        session['usr'] = username
        session['pass'] = password
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+';UID='+username+ ';PWD='+ password)
        cursor=cnxn.cursor()
        cnxn.close()
    except:
        flash('Datos incorrectos')
    return render_template('Comunes/principal.html')





#Muestra el usuario que ingreso al sistema (USUARIOS DIRECTOS DE SQL)
@app.route('/Usuario', methods=['POST'])
def Usuario():
    try:
        server = 'localhost'
        database = 'ERP2020'
        username = session['usr']
        password = session['pass']
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        usr = session['usr']
        interface = "Principal"
        est = ("", "", "")
        session['bandera'] = 1
    except:
        flash('Sesion terminada')
    return render_template('Comunes/principal.html', usuario=usr, interfaz=interface, estado=est)







#Direccionamiento de interfaces:

@app.route('/cerrarSesion')
def cerrarSesion():
    return render_template('Login.html')

@app.route('/Regresar')
def Regresar():
    return render_template('Comunes/principal.html')

@app.route('/Deducciones')
def Deducciones():
    return render_template('Deducciones/Deducciones.html')

@app.route('/Percepciones')
def Percepcciones():
    return render_template('Percepciones/ConsultaGeneralPercepciones.html')

@app.route('/Ciudades')
def Ciudades():
    return render_template('Ciudades/ConsultaGeneralCiudad.html')

@app.route('/Estado')
def Estado():
    return render_template('Estado/ConsultaGeneralEstado.html')







                                                    #Diferentes consultas para las DEDUCCIONES:

@app.route('/NuevaDeduccion')
def NuevaDeduccion():
    return render_template('Deducciones/NuevaDeduccion.html')


@app.route('/CancelarD')
def CancelarDeduccion():
    return render_template('Deducciones/Deducciones.html')


#Insertar una Nueva Deduccion
@app.route('/insertarDeduccion', methods=['POST'])
def insertarDeduccion():
        id=request.form['id']
        nombreDe=request.form['nombre']
        descripcion=request.form['descripcion']
        porcentaje=request.form['porcentaje']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Deducciones (idDeduccion, nombre, descripcion, porcentaje) VALUES (?, ?, ?, ?);',
                    (id,nombreDe,descripcion,porcentaje))
        conn.commit()
        return render_template('Deducciones/Deducciones.html')



#Lista General de Deducciones
@app.route('/listarDeducciones')
def listarDeducciones():
        cursor = conn.cursor()
        cursor.execute('Select * from RH.Deducciones;')
        data = cursor.fetchall()
        return render_template('Deducciones/Deducciones.html', deducciones=data)



#Lista Individual de deducciones
@app.route('/seleccionDeducciones', methods=['POST'])
def seleccionDeducciones():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute('Select idDeduccion, nombre, descripcion, porcentaje from RH.Deducciones where idDeduccion={0}'.format(codigo))
    data = cursor.fetchall()
    return render_template('Deducciones/Deducciones.html', deducciones=data)




#Eliminar algun registro de las deducciones
@app.route('/eliminarDeduccion/<string:id>')
def eliminarDeduccion(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Deducciones where idDeduccion={0}'.format(id))
    conn.commit()
    return render_template('Deducciones/Deducciones.html')



#Editar deducciones
@app.route('/editarDeduccion/<id>')
def editarDeduccion(id):
    cursor = conn.cursor()
    cursor.execute('Select idDeduccion, nombre, descripcion, porcentaje from RH.Deducciones where idDeduccion={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Deducciones/EditarDeduccion.html', deduccion=data[0])



#Actualizar el registro editado
@app.route('/actualizarDeduccion/<id>', methods=['POST'])
def actualizarDeduccion(id):
    idD=request.form['id']
    nombre=request.form['nombre']
    descripcion=request.form['descripcion']
    porcentaje=request.form['porcentaje']
    cursor = conn.cursor()
    cursor.execute('Update RH.Deducciones set idDeduccion=?, nombre=?, descripcion=?, porcentaje=? where idDeduccion=?;'
                   ,(idD, nombre,descripcion,porcentaje,id))
    conn.commit()
    return render_template('Deducciones/Deducciones.html')






                                                        # Diferentes consultas para las Percepciones

@app.route('/NuevaPercepcion')
def NuevaPercepcion():
    return render_template('Percepciones/NuevaPercepcion.html')

@app.route('/CancelarP')
def CancelarPercepcion():
    return render_template('/Percepciones/ConsultaGeneralPercepciones.html')



    # Insertar una Nueva Percepcion
@app.route('/insertarPercepcion', methods=['POST'])
def insertarPercepcion():
        id = request.form['id']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        diasP=request.form['diaspagar']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Percepciones (idPercepcion, nombre, descripcion, diasPagar) VALUES (?, ?, ?, ?);',
            (id, nombre, descripcion, diasP))
        conn.commit()
        return render_template('Percepciones/ConsultaGeneralPercepciones.html')



        # Lista General de Percepciones
@app.route('/listarPercepciones')
def listarPercepciones():
    cursor = conn.cursor()
    cursor.execute('Select idPercepcion, nombre, descripcion, diasPagar from RH.Percepciones')
    data = cursor.fetchall()
    return render_template('Percepciones/ConsultaGeneralPercepciones.html', percepciones=data)



    # Lista Individual de Percepciones
@app.route('/seleccionPercepciones', methods=['POST'])
def seleccionPercepciones():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select idPercepcion, nombre, descripcion, diasPagar from RH.Percepciones where idPercepcion={0}'.format(
            codigo))
    data = cursor.fetchall()
    return render_template('Percepciones/ConsultaGeneralPercepciones.html', percepciones=data)



    # Eliminar algun registro de las Percepciones
@app.route('/eliminarPercepcion/<string:id>')
def eliminarPercepcion(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Percepciones where idPercepcion={0}'.format(id))
    conn.commit()
    return render_template('Percepciones/ConsultaGeneralPercepciones.html')



    # Editar Percepciones
@app.route('/editarPercepcion/<id>')
def editarPercepcion(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select idPercepcion, nombre, descripcion, diasPagar from RH.Percepciones where idPercepcion={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Percepciones/EditarPercepcion.html', perce=data[0])



    # Actualizar el registro editado
@app.route('/actualizarPercepcion/<id>', methods=['POST'])
def actualizarPercepcion(id):
    idP = request.form['id']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    diasP = request.form['diaspagar']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Percepciones set idPercepcion=?, nombre=?, descripcion=?, diasPagar=? where idPercepcion=?;'
        , (idP, nombre, descripcion, diasP, id))
    conn.commit()
    return render_template('Percepciones/ConsultaGeneralPercepciones.html')






                                                    #Diferentes consultas para las CIUDADES:
@app.route('/nuevaCiudad')
def nuevaCiudad():
    return render_template('Ciudades/NuevaCiudad.html')


@app.route('/CancelarC')
def CancelarCiudades():
    return render_template('Ciudades/ConsultaGeneralCiudad.html')



    # Insertar una Nueva Ciudad
@app.route('/insertarCiudad', methods=['POST'])
def insertarCiudad():
   # id = request.form['id']
    nombre = request.form['nombre']
    idestado = request.form['idestado']
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO RH.Ciudades (nombre, Estado_idEstado) VALUES (?, ?);',
        (nombre, idestado))
    conn.commit()
    return render_template('Ciudades/ConsultaGeneralCiudad.html')



# Lista General de Ciudades
@app.route('/listarCiudades')
def listarCiudades():
    cursor = conn.cursor()
    cursor.execute('Select idCiudad, nombre, Estado_idEstado from RH.Ciudades')
    data = cursor.fetchall()
    return render_template('Ciudades/ConsultaGeneralCiudad.html', ciudades=data)



    # Lista Individual de Ciudades
@app.route('/seleccionCiudades', methods=['POST'])
def seleccionCiudades():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select idCiudad, nombre, Estado_idEstado from RH.Ciudades where idCiudad={0}'.format(
            codigo))
    data = cursor.fetchall()
    return render_template('Ciudades/ConsultaGeneralCiudad.html', ciudades=data)



 # Eliminar algun registro de las Ciudades
@app.route('/eliminarCiudad/<string:id>')
def eliminarCiudad(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Ciudades where idCiudad={0}'.format(id))
    conn.commit()
    return render_template('Ciudades/ConsultaGeneralCiudad.html')



# Editar Ciudad
@app.route('/editarCiudad/<id>')
def editarCiudad(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select idCiudad, nombre, Estado_idEstado from RH.Ciudades where idCiudad={0}'.format(
            id))
    data = cursor.fetchall()
    return render_template('Ciudades/EditarCiudad.html', ciuda=data[0])




    # Actualizar el registro editado
@app.route('/actualizarCiudad/<id>', methods=['POST'])
def actualizarCiudad(id):
   # idc = request.form['id']
    nombre = request.form['nombre']
    idEstado = request.form['idEstado']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Ciudades set nombre=?, Estado_idEstado=? where idCiudad=?;'
         , (nombre,idEstado, id))
    conn.commit()
    return render_template('Ciudades/ConsultaGeneralCiudad.html')






                                              # Diferentes consultas para los ESTADOS:
@app.route('/nuevoEstado')
def nuevoEstado():
    return render_template('Estado/NuevoEstado.html')


@app.route('/CancelarE')
def CancelarEstado():
    return render_template('Estado/ConsultaGeneralEstado.html')



#Insertar una Nuevo Estado
@app.route('/insertarEstado', methods=['POST'])
def insertarEstado():
  #  id=request.form['id']
    nombre=request.form['nombre']
    siglas=request.form['siglas']
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO RH.Estado (nombre, siglas) VALUES (?, ?);', (nombre,siglas))
    conn.commit()
    return render_template('Estado/ConsultaGeneralEstado.html')



# Lista General de Estados
@app.route('/listarEstado')
def listarEstados():
    cursor = conn.cursor()
    cursor.execute('Select idEstado, nombre, siglas from RH.Estado')
    data = cursor.fetchall()
    return render_template('Estado/ConsultaGeneralEstado.html', estados=data)



# Lista Individual de Estados
@app.route('/seleccionEstado', methods=['POST'])
def seleccionEstado():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select idEstado, nombre, siglas from RH.Estado where idestado={0}'.format(codigo))
    data = cursor.fetchall()
    return render_template('Estado/ConsultaGeneralEstado.html', estados=data)



 # Eliminar algun registro de los Estados
@app.route('/eliminarEstado/<string:id>')
def eliminarEstado(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Estado where idEstado={0}'.format(id))
    conn.commit()
    return render_template('Estado/ConsultaGeneralEstado.html')



# Editar Estado
@app.route('/editarEstado/<id>')
def editarEstado(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select idEstado, nombre, siglas from RH.Estado where idEstado={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Estado/EditarEstado.html', estado=data[0])




# Actualizar el registro editado
@app.route('/actualizarEstado/<id>', methods=['POST'])
def actualizarEstado(id):
   # idc = request.form['id']
    nombre = request.form['nombre']
    siglas = request.form['siglas']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Estado set nombre=?, siglas=? where idEstado=?;'
         , (nombre,siglas, id))
    conn.commit()
    return render_template('Estado/ConsultaGeneralEstado.html')



if __name__ == '__main__':
    app.run(debug=True)
