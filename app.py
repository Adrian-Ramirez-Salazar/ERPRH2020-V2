#import pypyodbc
from flask import Flask, render_template, request, session, flash
from flask_paginate import Pagination, get_page_args
#from flask_sqlalchemy import SQLAlchemy
import pyodbc
#from sqlalchemy.sql.functions import session_user
from werkzeug.utils import redirect
#from Datos.DeduccionesDAO import DeduccionesDAO
#from Datos.usuarioDAO import UsuarioDAO
from Datos.Conexion import Conexion

app = Flask(__name__)

users = list(range(50))

def get_users(offset=0, per_page=10):
    return users[offset: offset + per_page]

app.secret_key=b'yangars'

conn = pyodbc.connect('Driver={SQL Server};'
<<<<<<< HEAD
                      'Server=DESKTOP-8SKO2G9\SQLEXPRESS;'
=======
                      'Server=DESKTOP-7SLALA5\SQLEXPRESS;'
>>>>>>> 57633791dbf063cec196fb37a10f56cc3e080159
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







#Direccionamiento y vista general de datos e interfaces:

@app.route('/cerrarSesion')
def cerrarSesion():
    return render_template('Login.html')


@app.route('/Regresar')
def Regresar():
    return render_template('Comunes/principal.html')


@app.route('/Deducciones')
def Deducciones():
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM RH.Deducciones;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Deducciones/Deducciones.html',
                           deducciones=reg,
                           page = page,
                           per_page = per_page,
                           pagination = pagination)



@app.route('/Percepciones')
def Percepcciones():
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM RH.Percepciones;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Percepciones/ConsultaGeneralPercepciones.html',
                           percepciones=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination
                           )



@app.route('/Ciudades')
def Ciudades():
    cursor = conn.cursor()
    cursor.execute('Select c.idCiudad,c.nombre, e.nombre from RH.Ciudades c join RH.Estado e on c.Estado_idEstado=E.idEstado;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Ciudades/ConsultaGeneralCiudad.html',
                           ciudades=reg,
                           page = page,
                           per_page = per_page,
                           pagination = pagination)



@app.route('/Estado')
def Estado():
    cursor = conn.cursor()
    cursor.execute('SELECT idEstado, nombre, siglas from  RH.Estado;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Estado/ConsultaGeneralEstado.html',
                           estados= reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



@app.route('/Puestos')
def Puestos():
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM RH.Puestos;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Puestos/ConsultaGeneralPuestos.html',
                           puestos=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



@app.route('/Horarios')
def Horarios():
    cursor = conn.cursor()
    cursor.execute('Select h.idHorario,h.horaInicio,h.horaFin, h.dias, e.nombre+' '+e.apaterno+' '+e.amaterno from RH.Horarios h join  RH.Empleados e on e.idEmpleado=h.idEmpleado;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Horarios/ConsultaGeneralHorarios.html',
                           horarios=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



@app.route('/Empleados')
def Empleados():
    cursor = conn.cursor()
    cursor.execute('Select *from RH.Empleados;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Empleados/ConsultaGeneralEmpleados.html',
                           empleados=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



@app.route('/Departamentos')
def Departamentos():
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM RH.Departamentos;')
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    return render_template('Departamentos/ConsultaGeneralDepartamentos.html',
                           departamentos=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)




                                                    #Diferentes consultas para las DEDUCCIONES:

@app.route('/NuevaDeduccion')
def NuevaDeduccion():
    return render_template('Deducciones/NuevaDeduccion.html')


#Insertar una Nueva Deduccion
@app.route('/insertarDeduccion', methods=['POST'])
def insertarDeduccion():
       # id=request.form['id']
        nombreDe=request.form['nombre']
        descripcion=request.form['descripcion']
        porcentaje=request.form['porcentaje']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Deducciones (nombre, descripcion, porcentaje) VALUES (?, ?, ?);',
                    (nombreDe,descripcion,porcentaje))
        conn.commit()
        return redirect('/Deducciones')




#Lista Individual de deducciones
@app.route('/seleccionDeducciones', methods=['POST'])
def seleccionDeducciones():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute('Select idDeduccion, nombre, descripcion, porcentaje from RH.Deducciones where idDeduccion={0}'.format(codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Deducciones/Deducciones.html',
                           deducciones=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)




#Eliminar algun registro de las deducciones
@app.route('/eliminarDeduccion/<string:id>')
def eliminarDeduccion(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Deducciones where idDeduccion={0}'.format(id))
    conn.commit()
    return redirect('/Deducciones')




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
   # idD=request.form['id']
    nombre=request.form['nombre']
    descripcion=request.form['descripcion']
    porcentaje=request.form['porcentaje']
    cursor = conn.cursor()
    cursor.execute('Update RH.Deducciones set nombre=?, descripcion=?, porcentaje=? where idDeduccion=?;'
                   ,(nombre,descripcion,porcentaje,id))
    conn.commit()
    return redirect('/Deducciones')









                                                        # Diferentes consultas para las Percepciones

@app.route('/NuevaPercepcion')
def NuevaPercepcion():
    return render_template('Percepciones/NuevaPercepcion.html')



    # Insertar una Nueva Percepcion
@app.route('/insertarPercepcion', methods=['POST'])
def insertarPercepcion():
       # id = request.form['id']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        diasP=request.form['diaspagar']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Percepciones (nombre, descripcion, diasPagar) VALUES ( ?, ?, ?);',
            (nombre, descripcion, diasP))
        conn.commit()
        return redirect('/Percepciones')




    # Lista Individual de Percepciones
@app.route('/seleccionPercepciones', methods=['POST'])
def seleccionPercepciones():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select idPercepcion, nombre, descripcion, diasPagar from RH.Percepciones where idPercepcion={0}'.format(
            codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Percepciones/ConsultaGeneralPercepciones.html',
                           percepciones=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)




    # Eliminar algun registro de las Percepciones
@app.route('/eliminarPercepcion/<string:id>')
def eliminarPercepcion(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Percepciones where idPercepcion={0}'.format(id))
    conn.commit()
    return redirect('/Percepciones')



    # Editar Percepciones
@app.route('/editarPercepcion/<id>')
def editarPercepcion(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select  nombre, descripcion, diasPagar from RH.Percepciones where idPercepcion={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Percepciones/EditarPercepcion.html', perce=data[0])




    # Actualizar el registro editado
@app.route('/actualizarPercepcion/<id>', methods=['POST'])
def actualizarPercepcion(id):
   # idP = request.form['id']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    diasP = request.form['diaspagar']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Percepciones set nombre=?, descripcion=?, diasPagar=? where nombre=?;'
        , (nombre, descripcion, diasP, id))
    conn.commit()
    return redirect('/Percepciones')










                                                    #Diferentes consultas para las CIUDADES:
@app.route('/nuevaCiudad')
def nuevaCiudad():
    return render_template('Ciudades/NuevaCiudad.html')



    # Insertar una Nueva Ciudad
@app.route('/insertarCiudad', methods=['POST'])
def insertarCiudad():
    try:
        # id = request.form['id']
        nombre = request.form['nombre']
        idestado = request.form['idestado']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Ciudades (nombre, Estado_idEstado) VALUES (?, ?);',
            (nombre, idestado))
        conn.commit()
    except:
       return ('REGISTROS INEXISTENTES: NO HAY RELACION CON LOS ESTADOS')
    return redirect('/Ciudades')




    # Lista Individual de Ciudades
@app.route('/seleccionCiudades', methods=['POST'])
def seleccionCiudades():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select idCiudad, nombre, Estado_idEstado from RH.Ciudades where idCiudad={0}'.format(
            codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Ciudades/ConsultaGeneralCiudad.html',
                           ciudades=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



 # Eliminar algun registro de las Ciudades
@app.route('/eliminarCiudad/<string:id>')
def eliminarCiudad(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Ciudades where idCiudad={0}'.format(id))
    conn.commit()
    return redirect('/Ciudades')



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
    return redirect('/Ciudades')








                                                         # Diferentes consultas para los ESTADOS:
@app.route('/nuevoEstado')
def nuevoEstado():
    return render_template('Estado/NuevoEstado.html')



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
    return redirect('/Estado')





# Lista Individual de Estados
@app.route('/seleccionEstado', methods=['POST'])
def seleccionEstado():
        codigo = request.form['codigoBarras']
        cursor = conn.cursor()
        cursor.execute(
            'Select idEstado, nombre, siglas from RH.Estado where idestado={0}'.format(codigo))
        data = cursor.fetchall()
        page, per_page, offset = get_page_args(page_parameter='page',
                                            per_page_parameter='per_page')
        total = len(users)
        pagination_users = get_users(offset=offset, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')

        if data:
            reg = data
        else:
            return '<h1>NO EXISTE EL REGISTRO</h1>'

        return render_template('Estado/ConsultaGeneralEstado.html',
                            estados= reg,
                            page=page,
                            per_page=per_page,
                            pagination=pagination)



 # Eliminar algun registro de los Estados
@app.route('/eliminarEstado/<string:id>')
def eliminarEstado(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Estado where idEstado={0}'.format(id))
    conn.commit()
    return redirect('/Estado')



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
    return redirect('/Estado')









                                                        #DIFERENTES CONSULTAS PARA LOS PUESTOS
#nuevo Puesto
@app.route('/nuevoPuesto')
def nuevoPuesto():
    return render_template('Puestos/NuevoPuesto.html')



#Insertar un nuevo Puesto
@app.route('/insertarPuesto', methods=['POST'])
def insertarPuesto():
    nombre = request.form['nombrePuesto']
    salarioMin = request.form['SALARIOMIN']
    salarioMax = request.form['SALARIOMAX']
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO RH.Puestos (nombre, salarioMinimo, salarioMaximo) VALUES (?,?,?)',(nombre,salarioMin,salarioMax))
    conn.commit()
    return redirect('/Puestos')




# Lista Individual de Puestos
@app.route('/seleccionPuesto', methods=['POST'])
def seleccionPuesto():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select *from RH.Puestos where idPuesto={0}'.format(codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Puestos/ConsultaGeneralPuestos.html',
                           puestos=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)



 # Eliminar algun registro de los Puestos
@app.route('/eliminarPuesto/<string:id>')
def eliminarPuesto(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Puestos where idPuesto={0}'.format(id))
    conn.commit()
    return redirect('/Puestos')



# Editar Puesto
@app.route('/editarPuesto/<id>')
def editarPuesto(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select idPuesto, nombre, salarioMinimo, salarioMaximo from RH.Puestos where idPuesto={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Puestos/EditarPuesto.html', puesto=data[0])



# Actualizar el registro editado
@app.route('/actualizarPuesto/<id>', methods=['POST'])
def actualizarPuesto(id):
    nombre = request.form['nombrePuesto']
    salarioMIN = request.form['SALARIOMIN']
    salarioMAX = request.form['SALARIOMAX']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Puestos set nombre=?, salarioMinimo=?, salarioMaximo=? where idPuesto=?;'
         , (nombre,salarioMIN, salarioMAX, id))
    conn.commit()
    return redirect('/Puestos')









                                                        #DIFERENTES CONSULTAS PARA LOS HORARIOS

#nuevo horario
@app.route('/NuevoHorario')
def nuevoHorario():
    return render_template('Horarios/NuevoHorario.html')



#Insertar un nuevo Horario
@app.route('/insertarHorario', methods=['POST'])
def insertarHorario():
    try:
        horaInicio = request.form['horaInicio']
        horaFin = request.form['horaFin']
        dias = request.form['Dias']
        idE = request.form['idEmple']
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO RH.Horarios (horaInicio, horaFin, dias,idEmpleado) VALUES (?,?,?,?)',(horaInicio,horaFin,dias,idE))
        conn.commit()
    except:
        return ('NO EXISTE RELACION CON ALGUN EMPLEADO: ID INCORRECTO')
    return redirect('/Horarios')





# Lista Individual de Horarios
@app.route('/seleccionHorario', methods=['POST'])
def seleccionHorarios():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
       'Select *from RH.Horarios where idHorario={0}'.format(codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Horarios/ConsultaGeneralHorarios.html',
                           horarios=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)




# Eliminar algun registro de los Horarios
@app.route('/EliminarHorario/<string:id>')
def eliminarHorario(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Horarios where idHorario={0}'.format(id))
    conn.commit()
    return redirect('/Horarios')




# Editar Horario
@app.route('/EditarHorario/<id>')
def editarHorario(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select * from RH.Horarios where idHorario={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Horarios/EditarHorario.html', hor=data[0])



# Actualizar el registro editado
@app.route('/actualizarhorario/<id>', methods=['POST'])
def actualizarHorario(id):
    horaInicio = request.form['horaInicio']
    horaFin = request.form['horaFin']
    dias = request.form['Dias']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Horarios set horaInicio=?, horaFin=?, dias=? where idHorario=?;', (horaInicio,horaFin,dias, id))
    conn.commit()
    return redirect('/Horarios')









                                                                #DIFERENTES CONSULTAS PARA LOS EMPLEADOS

#nuevo Empleado
@app.route('/nuevoEmpleado')
def nuevoEmpleado():
    return render_template('Empleados/nuevoEmpleado.html')


#Insertar un nuevo empleado
@app.route('/insertarEmpleado', methods=['POST'])
def insertarEmpleado():
    try:
        nombre = request.form['nombre']
        apaterno = request.form['apaterno']
        amaterno = request.form['amaterno']
        sexo = request.form['sexo']
        feContratacion = request.form['fechaContratacion']
        feNacimiento = request.form['fechaNacimiento']
        salario = request.form['salario']
        seguroSocial = request.form['nss']
        estadoCivil = request.form['estadoCivil']
        diasVaca = request.form['diasVacaciones']
        diasPermiso = request.form['diasPermiso']
        foto = request.files['foto'].stream.read()
        direccion = request.form['direccion']
        colonia = request.form['colonia']
        codigoPostal = request.form['codigoPostal']
        escolaridad = request.form['escolaridad']
        comision = request.form['porcentajeComision']
        idDepa = request.form['idDepa']
        idPuesto = request.form['idPuesto']
        idCiudad = request.form['city']
        cursor = conn.cursor()
        cursor.execute(
            'Insert into RH.Empleados (nombre,apaterno,amaterno,sexo,fechaContratacion,fechaNacimiento,salario,nss,estadoCivil,diasVacaciones,diasPermiso,'
            'fotografia,direccion,colonia,codigoPostal,escolaridad,porcentajeComision,idDepartamento,idPuesto,idCiudad) '
            'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);', (nombre,apaterno,amaterno,sexo,feContratacion,feNacimiento,salario,seguroSocial,
                                                     estadoCivil,diasVaca,diasPermiso,foto,direccion,colonia,codigoPostal,escolaridad,
                                                     comision,idDepa,
                                                     idPuesto,
                                                     idCiudad))
        conn.commit()
    except:
        return ('ALGUN CAMPO HACE REFERENCIA A UN REGISTRO INEXISTENTE.')
    return redirect('/Empleados')




# Lista Individual de Empleados
@app.route('/seleccionEmpleados', methods=['POST'])
def seleccionEmpleados():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute('Select idEmpleado, nombre, apaterno, amaterno, sexo, fechaContratacion,'
                   ' fechaNacimiento, salario,nss, estadoCivil, diasVacaciones, diasPermiso, fotografia, direccion, colonia,'
                    'codigoPostal, escolaridad, porcentajeComision from RH.Empleados where idEmpleado={0}'.format(codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Empleados/ConsultaGeneralEmpleados.html',
                           empleados=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)




# Eliminar algun registro de los Empleados
@app.route('/eliminarEmpleado/<string:id>')
def eliminarEmpleado(id):
    try:
        cursor = conn.cursor()
        cursor.execute('Delete from RH.Empleados where idEmpleado={0}'.format(id))
        conn.commit()
    except:
        return 'No se puede eliminar el EMPLEADO ya que esta asignado a un HORARIO: Elimine el Horario asignado primero'
    return redirect('/Empleados')




# Editar Empleado
@app.route('/editarEmpleado/<id>')
def editarEmpleado(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select *from RH.Empleados where idEmpleado={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Empleados/editarEmpleado.html', emple=data[0])



@app.route("/consultaImagen/<id>")
def consultaImagen(id):
    img = Conexion.consultarFoto(id)
    return img


    # Actualizar el registro editado
@app.route('/actualizarEmpleado/<id>', methods=['POST'])
def actualizarEmpleado(id):
    nombre = request.form['nombre']
    apaterno = request.form['apaterno']
    amaterno = request.form['amaterno']
    sexo = request.form['sexo']
    fechaContratacion = request.form['fechaContratacion']
    fechaNacimiento = request.form['fechaNacimiento']
    salario = request.form['salario']
    nss = request.form['nss']
    estadoCivil = request.form['estadoCivil']
    diasVacaciones = request.form['diasVacaciones']
    diasPermiso = request.form['diasPermiso']
    fotografia = request.files['foto'].stream.read()
    direccion = request.form['direccion']
    colonia = request.form['colonia']
    codigoPostal = request.form['codigoPostal']
    escolaridad = request.form['escolaridad']
    porcentajeComision = request.form['porcentajeComision']
    idDepa = request.form['idDepa']
    idPuesto = request.form['idPuesto']
    city = request.form['city']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Empleados set nombre=?, apaterno=?, amaterno=?, sexo=?, fechaContratacion=?, fechaNacimiento=?, salario=?,'
        'nss=?, estadoCivil=?, diasVacaciones=?, diasPermiso=?, fotografia=?, direccion=?, colonia=?, codigoPostal=?, escolaridad=?,'
        'porcentajeComision=?, idDepartamento=?, idPuesto=?, idCiudad=?  where idEmpleado=?;', (nombre,apaterno,amaterno,sexo,fechaContratacion,
                                                                                                fechaNacimiento,salario,nss,estadoCivil,
                                                                                                diasVacaciones,diasPermiso,fotografia,
                                                                                                direccion,colonia,codigoPostal,escolaridad,
                                                                                                porcentajeComision,idDepa,idPuesto,city,id))
    conn.commit()
    return redirect('/Empleados')








                                                         #DIFERENTES CONSULTAS PARA LOS DEPARTAMENTOS

#nuevo Departamento
@app.route('/nuevoDepartamento')
def nuevoDepartamento():
    return render_template('Departamentos/NuevoDepartamento.html')



#Insertar un nuevo Departamento
@app.route('/insertarDepartamento', methods=['POST'])
def insertarDepartamento():
    #id = request.form['id']
    nombreDepa = request.form['nombreDepa']
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO RH.Departamentos (nombre) VALUES (?)',(nombreDepa))
    conn.commit()
    return redirect('/Departamentos')




# Lista Individual de Departamentos
@app.route('/seleccionDepartamento', methods=['POST'])
def seleccionDepartamento():
    codigo = request.form['codigoBarras']
    cursor = conn.cursor()
    cursor.execute(
        'Select *from RH.Departamentos where idDepartamento={0}'.format(codigo))
    data = cursor.fetchall()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(users)
    pagination_users = get_users(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    if data:
        reg = data
    else:
        return '<h1>NO EXISTE EL REGISTRO</h1>'
    return render_template('Departamentos/ConsultaGeneralDepartamentos.html',
                           departamentos=reg,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)





 # Eliminar algun registro de los Departamentos
@app.route('/eliminarDepartamento/<string:id>')
def eliminarDepartamento(id):
    cursor = conn.cursor()
    cursor.execute('Delete from RH.Departamentos where idDepartamento={0}'.format(id))
    conn.commit()
    return redirect('/Departamentos')




# Editar Departamento
@app.route('/editarDepartamento/<id>')
def editarDepartamento(id):
    cursor = conn.cursor()
    cursor.execute(
        'Select nombre from RH.Departamentos where idDepartamento={0}'.format(id))
    data = cursor.fetchall()
    return render_template('Departamentos/EditarDepartamento.html', depa=data[0])




# Actualizar el registro editado
@app.route('/actualizarDepartamento/<id>', methods=['POST'])
def actualizarDepartamento(id):
    nombre = request.form['nombreD']
    cursor = conn.cursor()
    cursor.execute(
        'Update RH.Departamentos set nombre=? where nombre=?;' , (nombre, id))
    conn.commit()
    return redirect('/Departamentos')



if __name__ == '__main__':
    app.run(debug=True)
