#from flask import Flask,render_template,request, flash
#import sqlite3
#from db import get_db
#from _sqlite3 import Error

import functools
import os
from re import X

from flask import Flask, render_template, request, flash,redirect, url_for, session, send_file, current_app, g, make_response


from db import get_db, close_db
from jinja2 import Environment, FileSystemLoader,Template
app = Flask( __name__ )
app.secret_key = os.urandom( 24 )
import numpy as np
import random

THIS_DIR = os.path.dirname(os.path.abspath(__file__))



app = Flask(__name__)
app.secret_key = os.urandom( 24 )

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/sesion')
def sesion():
    return render_template('inicio.html')

@app.route('/pagina1')
def pagina1():
    return render_template('iniciar_sesion.html')

@app.route('/pagina2')
def pagina2():
    return render_template('registro.html')

@app.route('/politicas')
def politicas():
    return render_template('politicas.html')

@app.route('/perfil')
def perfil():
    return render_template('mi_perfil.html')

@app.route('/deseos1')
def deseos1():
    return render_template('lista_deseos1.html')

@app.route( '/login', methods=('GET', 'POST') )
def login():
    global var
    try:
        if request.method == 'POST':

            username = request.form['username']
            password = request.form['password']
            
            if not username:
                error = 'Debes ingresar el usuario'
                print(error)
                flash( error )
                return render_template( 'iniciar_sesion.html' )
            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'iniciar_sesion.html' )
            db=get_db()
            user = db.execute(
                    'SELECT * FROM usuarios WHERE username=? and contrasena=? ', (username,password)
            ).fetchone() 
            db.commit()
            if user is None:
                print('Usuario o contraseña inválidos')
            else:
                print("usuario valido")
                roles = db.execute('SELECT id_rol FROM usuarios WHERE username=?', (username,)).fetchone()
                registroRoles=str(roles[0])
                print(registroRoles)
                db.commit()

                if registroRoles=='3':
                    print(registroRoles)
                    #return render_template('perfiles.html')
                    #return (perfiles())
                    var=username
                    print(var)
                    return mi_perfil()

                if registroRoles=='1':
                    print(registroRoles)
                    #return render_template('perfiles.html')
                    #return (perfiles())
                    var=username
                    print(var)
                    return superUsuarios()
        return render_template( 'iniciar_sesion.html' )
    except:
        return render_template( 'iniciar_sesion.html' )
        

@app.route( '/register', methods=('GET', 'POST') )
def register():
    """return render_template( 'iniciar_sesion.html' )"""
    try:
        

        if request.method == 'POST':
            option='0'
            name= request.form['nombre2']
            apellido= request.form['apellido2']
            genero=request.form['genero']
            cedula= request.form['cedula2']
            direccion= request.form['direccion2']
            correo= request.form['correo2']
            username = request.form['usuario2']
            password = request.form['passwd']
            option = request.form['terminos']
            option2=str(option)
            rol='3'
            estado='1'
            ciudad='146'
            db=get_db()
            #print(option2)
            
            #return render_template( 'inicio.html' )
            #"print('resultados')"
            #print(name+apellido+genero+cedula+direccion+correo+username+password)   
            
            #registro=db.execute('SELECT id FROM genero WHERE nombre= ?', (genero,)).fetchone()
            #registro=db.execute('SELECT cedula FROM usuarios WHERE nombre= ?', (name,)).fetchone()
            


            dato=db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchone() 
            registro=str(dato[0])
            db.commit()

            if not name:
                error = 'nombre  requerido'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not apellido:
                error = 'apellido  requerido'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not cedula:
                error = 'cedula  requerida'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not direccion:
                error = 'direccion  requerida'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not correo:
                error = 'correo  requerido'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not username:
                error = 'nombre de usuario requerido'
                #flash( error )
                print(error)
                render_template( 'registro.html' )
            if not password:
                error = 'contraseña  requerida'
                #flash( error )
                print(error)
                render_template( 'registro.html' )

            if db.execute( 'SELECT id_usuario FROM usuarios WHERE username = ?', (username,) ).fetchone() is not None:
                error = 'El nombre de usuario ya existe'.format('vacio')
                #error='datos no cumplen'
                #flash( error )
                print(error)
                db.commit()
                return render_template( 'registro.html' )
            
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE cedula = ?', (cedula,) ).fetchone() is not None:
                error = 'El usuario con mumero de cedula {sedu} ya existe'.format(sedu=cedula)
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'registro.html' )
            
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE email = ?', (correo,) ).fetchone() is not None:
                error = 'El correo {corr} ya existe'.format(corr=correo)
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'registro.html' )

            print(registro)
            print(name+apellido+genero+cedula+direccion+correo+username+genero+registro+rol+estado)

            if (option2=='1'):
                print(option2)  
                db.execute(
                    'INSERT INTO usuarios (username, nombre, apellido,cedula,email,direccion,contrasena,id_rol,id_genero,estadoU,ciudadU) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                    (username, name, apellido,cedula,correo,direccion,password,rol,registro,estado,ciudad)
                )
                db.commit()
                return render_template( 'iniciar_sesion.html' )
            
            

            

        return render_template( 'registro.html' )
        
    except:
        return render_template( 'registro.html' )

#@app.route('/usuarios')
#def usuarios():
 #   db=get_db()
  #  usuarios = db.execute('SELECT id_usuario, nombre, username, email FROM usuarios').fetchall()
    #nom=db.execute('SELECT  nombre FROM usuarios').fetchall()
   # return render_template('mi_perfil.html', my_string="Wheeeee!",usuarios=usuarios)


#@app.route("/nuevo")
#def template_test():
 #   return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

#@app.route("/mi_perfil")
#def mi_perfil():
 #   return render_template('mi_perfil.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


#@app.route("/perfiles")
#def perfiles():
#    return render_template('mi_perfil.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/mi_perfil")
def mi_perfil():
    db=get_db()
    #usuario = db.execute('SELECT  nombre FROM usuarios').fetchall()
    usuario=db.execute( 'SELECT nombre,apellido,cedula,id_genero,direccion,email,username FROM usuarios WHERE username = ?', (var,) ).fetchone() 
    
    global numCed

    username2=str(usuario[0])
    apellido=str(usuario[1])
    cedula=str(usuario[2])
    id_gen=str(usuario[3])
    direccion=str(usuario[4])
    correo=str(usuario[5])
    username=str(usuario[6])
    numCed=cedula
    datogen=db.execute( 'SELECT nombre FROM genero WHERE id = ?', (id_gen,) ).fetchone() 
    registroGen=str(datogen[0])

    print(username)
    db.commit()
    return render_template('mi_perfil.html',my_string="Wheeeee!",usuar=username2, apellido=apellido,cedula=cedula,registroGen=registroGen,direccion=direccion,correo=correo,username=username)

@app.route( '/modUser', methods=('GET', 'POST') )
def modUser():
    try:
        if request.method == 'POST':
            db=get_db()
            name= request.form['nombre2']
            apell=request.form['apellido']
            dir= request.form['direccion']
            corr= request.form['correo']
            user=request.form['usuario']
            genero=request.form['genero']
            #cedula= request.form['cedula2']
            #nom=str(cedula)
            #cedula=request.form['cedula']
            #print(nom)
            
            dato=db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchone() 
            registro=str(dato[0])
            db.commit()

            if not name:
                error = 'nombre  requerido'
                #flash( error )
                print(error)
                return mi_perfil()

            if not apell:
                error = 'apellido requerido'
                #flash( error )
                print(error)
                return mi_perfil()
            
            if not corr:
                error = 'Correo requerido'
                #flash( error )
                print(error)
                return mi_perfil()
            
            if not dir:
                error = 'Direccion requerida'
                #flash( error )
                print(error)
                return mi_perfil()
            
            if not user:
                error = 'Nombre de usuario requerido'
                #flash( error )
                print(error)
                return mi_perfil()

            if db.execute( 'SELECT id_usuario FROM usuarios WHERE username = ?', (user,) ).fetchone() is not None:
                error = 'El nombre de usuario ya existe'
                sql='''UPDATE usuarios SET nombre='{}',apellido='{}',direccion='{}',email='{}',id_genero='{}' WHERE cedula={}'''.format(name,apell,dir,corr,registro,numCed)
                db.execute(sql)
                db.commit()
                #flash(error)
                print(error)
                print(genero)
                return mi_perfil()


            sql='''UPDATE usuarios SET nombre='{}',apellido='{}',direccion='{}',email='{}',username='{}',id_genero='{}' WHERE cedula={}'''.format(name,apell,dir,corr,user,registro,numCed)
            db.execute(sql)
            db.commit()
            return render_template('iniciar_sesion.html')

        return render_template( 'iniciar_sesion.html' )
    except:
        return render_template( 'iniciar_sesion.html' )
#dato=db.execute( 'SELECT nombre FROM usuarios WHERE username = ?', (var,) ).fetchone() 
#username2=str(dato[0])
@app.route("/ruta")
def ruta():
    db=get_db()
    usuario=db.execute( 'SELECT direccion,ciudadU FROM usuarios WHERE username = ?', (var,) ).fetchone() 
    direccion2=str(usuario[0])
    ciudad2=str(usuario[1])
    municipio=db.execute( 'SELECT nombre,departamento FROM ciudades WHERE id = ?', (ciudad2,) ).fetchone() 
    munici=str(municipio[0])
    depart=str(municipio[1])
    print(direccion2)
    print(ciudad2)
    print(munici)
    print(depart)
    db.commit()
    return render_template('lista_deseos6.html',direccion2=direccion2,munici=munici,depart=depart)
   # return render_template('mi_perfil.html',my_string="Wheeeee!",usuar=username2, apellido=apellido,cedula=cedula,registroGen=registroGen,direccion=direccion,correo=correo,username=username)

@app.route( '/cambiar', methods=('GET', 'POST') )
def cambiar():
    
    try:
        if request.method == 'POST':
            db=get_db()
            contra= request.form['actual_pas']
            nuevaContra=request.form['nueva_pas']
            confirContra=request.form['confirmar_pas']

            usuarioContra=db.execute( 'SELECT contrasena FROM usuarios WHERE username = ?', (var,) ).fetchone() 
            contrasena=str(usuarioContra[0])
            db.commit()
            if not contra:
                error = 'Contraseña actual requerida'
                #flash( error )
                print(error)
                return render_template('cambiar_contrasena.html')

            if not nuevaContra:
                error = 'Nueva contraseña requerida'
                #flash( error )
                print(error)
                return render_template('cambiar_contrasena.html')
            if not confirContra:
                error = 'Confirmacion de contraseña requerida'
                #flash( error )
                print(error)
                return render_template('cambiar_contrasena.html')
            if (contra==nuevaContra):
                error = 'La contraseña nueva debe ser diferente a la actual'
                #flash( error )
                print(error)
                return render_template('cambiar_contrasena.html')

            if contra!=contrasena:
                print('La contrasena no es valida')
                return render_template('cambiar_contrasena.html')
            print(contra)
            
            if contra==contrasena:
                if nuevaContra==confirContra:
                    txcontra=str(nuevaContra)
                    print(nuevaContra)
                    print(confirContra)
                    print(var)
                    
                    sql='''UPDATE usuarios SET contrasena='{}' WHERE cedula={}'''.format(nuevaContra,numCed)
                    #sql='''UPDATE usuarios SET contrasena='{}' WHERE username={}'''.format(nuevaContra,var)
                    
                    db.execute(sql)
                    db.commit()
                    print('Cambio la contraseña con exito')
                    print(nuevaContra)
                    print(confirContra)
                    return render_template('iniciar_sesion.html')

        return render_template( 'cambiar_contrasena.html' )
    except:
        return render_template( 'cambiar_contrasena.html' )

@app.route('/deseos12')
def deseos12():
    return render_template('lista_desos2.html')

@app.route( '/deseos2', methods=('GET', 'POST') )
def deseos2():
    """return render_template( 'iniciar_sesion.html' )"""
    try:
        db=get_db()
        name= request.form['nombre2']
        if not name:
                error = 'nombre de la lista de deseos requerida'
                #flash( error )
                print(error)
                return render_template('lista_desos2.html')
        
        if db.execute( 'SELECT id FROM nombreLista WHERE nombre = ?', (name,) ).fetchone() is not None:
                error = 'La lista ya existe'
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'lista_desos2.html' )

        print(name)
        #nuevaContra='98765'
        #sql='''UPDATE usuarios SET contrasena='{}' WHERE cedula={}'''.format(nuevaContra,numCed)
        sql='''INSERT INTO nombreLista (nombre,username) VALUES ('{}', '{}')'''.format(name,var)
        db.execute(sql)
        db.commit()          
        return render_template( 'lista_desos2.html' )
    except:
        return render_template( 'lista_desos2.html' )

@app.route('/pagina50')
def pagina50():
    db=get_db()
    lista=db.execute( 'SELECT nombre FROM nombreLista WHERE username = ?', (var,) ).fetchall() 
    #print(str(lista[1]))
    valorList=[row[0]for row in lista]
    num=len(lista)
    print(num)
    db.commit()
    return render_template('lista_desos5.html',valorList=valorList)

@app.route( '/borrarLista', methods=('GET', 'POST') )
def borrarLista():
   
    try:
        if request.method == 'POST':
            db=get_db()
            lista=db.execute( 'SELECT nombre FROM nombreLista WHERE username = ?', (var,) ).fetchall() 
            #print(str(lista[1]))
            valorList=[row[0]for row in lista]
            num=len(lista)
            print(num)
            db.commit()
            return render_template('lista_desos51.html',valorList=valorList)
            

        return render_template( 'lista_desos5.html' )
    except:
        return render_template( 'lista_desos5.html' )

@app.route( '/pagina511', methods=('GET','POST') )
def pagina511():
    try:
        if request.method == 'POST':
            db=get_db()

            item= request.form['radioLista']
            dato=db.execute( 'SELECT id FROM nombreLista WHERE nombre = ?', (item,) ).fetchone() 
            registro=str(dato[0])
            sql='''DELETE FROM nombreLista WHERE id={}'''.format(registro)
            db.execute(sql)
            db.commit()
            print(item)
            
            #print(var)
            #print(registro)


           
            #print('Cambio la contraseña con exito')
            
            return borrarLista()

            
            return render_template('inicio.html')
        return borrarLista()
    except:
        return borrarLista()


@app.route( '/modificarLista', methods=('GET', 'POST') )
def modificarLista():
   
    try:
        if request.method == 'POST':
            db=get_db()
            lista=db.execute( 'SELECT nombre FROM nombreLista WHERE username = ?', (var,) ).fetchall() 
            #print(str(lista[1]))
            valorList=[row[0]for row in lista]
            num=len(lista)
            print(num)
            db.commit()
            return render_template('lista_desos52.html',valorList=valorList)
            

        return render_template( 'lista_desos5.html' )
    except:
        return render_template( 'lista_desos5.html' )


@app.route( '/pagina521', methods=('GET', 'POST') )
def pagina521():
   
    try:
        if request.method == 'POST':
            global valoritem2
            item2= request.form['radioLista']
            valoritem2=item2
            return render_template('lista_deseos7.html',item2=item2)
            

        return modificarLista()
    except:
        return modificarLista()


@app.route( '/pagina522', methods=('GET', 'POST') )
def pagina522():
   
    try:
        if request.method == 'POST':
            db=get_db()
            nombre= request.form['nombre']

            dato=db.execute( 'SELECT id FROM nombreLista WHERE nombre = ?', (valoritem2,) ).fetchone() 
            registro=str(dato[0])
            
            if not nombre:
                error = 'nombre de la lista de deseos requerida'
                #flash( error )
                print(error)
                return render_template('lista_deseos7.html')

            sql='''UPDATE nombreLista SET nombre='{}' WHERE id={}'''.format(nombre,registro)
                   
            
            db.execute(sql)
            db.commit()
            return modificarLista()
            

        return pagina521()
    except:
        return pagina521()

#SECCION DE SUPERADMINISTRADOR

@app.route("/superUsuarios")
def superUsuarios():
    db=get_db()
    usuarios = db.execute('SELECT id_usuario, nombre, username,cedula,email,id_genero,estadoU,id_rol,apellido FROM usuarios ').fetchall()
    id=[row[0]for row in usuarios]
    nombre=[row[1]for row in usuarios]
    username=[row[2]for row in usuarios]
    cedula=[row[3]for row in usuarios]
    email=[row[4]for row in usuarios]
    genero=[row[5]for row in usuarios]
    estado=[row[6]for row in usuarios]
    rol=[row[7]for row in usuarios]
    apellido=[row[8]for row in usuarios]
    num=len(id)
    print(num)
    valorLista=[]
    valorLista2=[]
    valorLista3=[]
    valorLista11=list()
    for i in range(num):
        nombregenero= db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero[i],) ).fetchall() 
        lista=[row[0]for row in nombregenero]
        #print(lista)
        valorLista.append(','.join(lista))
    
   # for i in range(num):
    #    valorLista11.append(','.join(valorLista[i]))
        
    for i in range(num):
        nombrerol= db.execute( 'SELECT nombre FROM roles WHERE idRol = ?', (rol[i],) ).fetchall() 
        lista2=[row[0]for row in nombrerol]
        #print(lista)
        valorLista2.append(','.join(lista2))
    
    for i in range(num):
        nombreestado= db.execute( 'SELECT nombre FROM estado WHERE id = ?', (estado[i],) ).fetchall() 
        lista3=[row[0]for row in nombreestado]
        #print(lista)
        valorLista3.append(','.join(lista3))



    print(valorLista[5])
    print(str(valorLista[7]))
    print(valorLista2[7])
    print(valorLista3[7])
    imprimir=','.join(valorLista[7])
    #arr = np.array([1, 2, 3, 4, 5])
    #np.append(arr, 10)   
    #lista=[row[0]for row in nombregenero]
    lista=[row[0]for row in nombregenero]
    #valor=[row[0]for row in nuewList]
    #print(nuewList)
    
    print(id+nombre+username+cedula+email+genero+estado+rol)
    conceptos = list(zip(id, nombre,apellido,username,cedula,email,valorLista,valorLista3,valorLista2))
    return render_template('superAdministrador_usuarios1.html', conceptos=conceptos,id=id, nombre=nombre, apellido=apellido,username=username,cedula=cedula,email=email,valorLista=valorLista,valorLista3=valorLista3,valorLista2=valorLista2,imprimir=imprimir)

@app.route("/adicionar_administradores")
def adicionar_administradores():
    return render_template('agregar_usuario2.html')

@app.route("/regresar")
def regresar():
    return superUsuarios()

@app.route( '/agregar1', methods=('GET', 'POST') )
def agregar1():
   
    try:
        if request.method == 'POST':
            db=get_db()
            nombre= request.form['nombre']
            apellido=request.form['apellido']
            cedula=request.form['identificacion']
            username=request.form['usuario']
            correo=request.form['correo']
            estado=request.form['estado']
            genero=request.form['genero']
            rol=request.form['tipo_usuario']

            if not nombre:
                error = 'Debes ingresar el nombre'
                print(error)
                flash( error )
                return render_template( 'agregar_usuario2.html' )
            
            if not apellido:
                error = 'Debes ingresar el apellido'
                print(error)
                flash( error )
                return render_template( 'agregar_usuario2.html' )

            if not cedula:
                error = 'Debes ingresar la cedula'
                print(error)
                flash( error )
                return render_template( 'agregar_usuario2.html' )

            if not username:
                error = 'Debes ingresar el nombre de usuario'
                print(error)
                flash( error )
                return render_template( 'agregar_usuario2.html' )
            
            if not correo:
                error = 'Debes ingresar el correo'
                print(error)
                flash( error )
                return render_template( 'agregar_usuario2.html' )
            
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE username = ?', (username,) ).fetchone() is not None:
                error = 'El nombre de usuario ya existe'.format('vacio')
                #error='datos no cumplen'
                #flash( error )
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )
            
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE cedula = ?', (cedula,) ).fetchone() is not None:
                error = 'El usuario con mumero de cedula {sedu} ya existe'.format(sedu=cedula)
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )
            
            if db.execute( 'SELECT id_usuario FROM usuarios WHERE email = ?', (correo,) ).fetchone() is not None:
                error = 'El correo {corr} ya existe'.format(corr=correo)
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )

            if estado=='selcategoria':
                error = 'Debes seleccionar un estado'
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )

            if genero=='selcategoria':
                error = 'Debes seleccionar un genero'
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )
            
            if rol=='selcategoria':
                error = 'Debes seleccionar un rol de usuario'
                #flash(error)
                print(error)
                db.commit()
                return render_template( 'agregar_usuario2.html' )

            estado2= db.execute( 'SELECT id FROM estado WHERE nombre = ?', (estado,) ).fetchall() 
            estado21=[row[0]for row in estado2]
            print(estado21[0])

            genero2= db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchall() 
            genero21=[row[0]for row in genero2]
            print(genero21[0])

            rol2= db.execute( 'SELECT idRol FROM roles WHERE nombre = ?', (rol,) ).fetchall() 
            rol21=[row[0]for row in rol2]
            print(rol21[0])

            direccion='MichaelKors corp'
            print(direccion)
            password = random.randint(1000000,9999999 )
            ciudad='146'
            print(password)
            print(nombre)
            print(apellido)
            print(cedula)
            print(username)
            print(correo)
            print(rol21[0])
            print(estado21[0])
            print(genero21[0])
            print(nombre+apellido+cedula+username+correo+str(rol21[0])+str(genero21[0])+str(estado21[0])+str(password))

            db.execute(
                    'INSERT INTO usuarios (username, nombre, apellido,cedula,email,direccion,contrasena,id_rol,id_genero,estadoU,ciudadU) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                    (username, nombre, apellido,cedula,correo,direccion,str(password),str(rol21[0]),str(genero21[0]),str(estado21[0]),ciudad)
                )
            db.commit()
            print('usuario creado')
            
            #print(nombre+apellido+cedula+username+correo+rol21+genero21+estado21+password)
            #print(nombre+apellido+cedula+username+correo)
            print(estado)
            return render_template('agregar_usuario2.html')
            
        return render_template('agregar_usuario2.html')
    except:
        return render_template('agregar_usuario2.html')



@app.route("/modificar1", methods=('GET', 'POST'))
def modificar1():
    try:
        if request.method == 'POST':
            db=get_db()
            radioselect= request.form['radioselect']
            radio= request.form['radio_horizontal']
            global newradio
            newradio=radio
            #print(radioselect)
            print(radio)
            #consultar o modificar usuario final
            if radioselect=='1':
                rol2= db.execute( 'SELECT id_rol,nombre,apellido,cedula,username,email,estadoU,id_genero,id_rol FROM usuarios WHERE id_usuario = ?', (radio,) ).fetchall() 
                
                rol21=[row[0]for row in rol2]
                rol212=[row[1]for row in rol2]
                rol213=[row[2]for row in rol2]
                rol214=[row[3]for row in rol2]
                rol215=[row[4]for row in rol2]
                rol216=[row[5]for row in rol2]
                rol217=[row[6]for row in rol2]
                rol218=[row[7]for row in rol2]
                rol219=[row[8]for row in rol2]
                print(rol212[0])
                nombre=str(rol212[0])
                apellido=str(rol213[0])
                cedula=str(rol214[0])
                username=str(rol215[0])
                email=str(rol216[0])
                estado=str(rol217[0])
                genero=str(rol218[0])
                rol=str(rol219[0])

                datoestado=db.execute( 'SELECT nombre FROM estado WHERE id = ?', (estado,) ).fetchone() 
                registroEstado=str(datoestado[0])

                datogenero=db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero,) ).fetchone() 
                registroGenero=str(datogenero[0])

                datorol=db.execute( 'SELECT nombre FROM roles WHERE idRol = ?', (rol,) ).fetchone() 
                registroRol=str(datorol[0])
                #print(registroGenero)
                #consultar o modificar usuario final
                if(str(rol21[0])=='3'):
                    dato='hola mundo'
                    print('usuario final')
                    return render_template('consultar_usuarios2.html',dato=dato, nombre=nombre, apellido=apellido, cedula=cedula,username=username,email=email,registroEstado=registroEstado,registroGenero=registroGenero,registroRol=registroRol)
                else:
                     #consultar o superAdministrador o administrador
                    return render_template('consultar_usuario3.html', nombre=nombre, apellido=apellido, cedula=cedula,username=username,email=email,registroEstado=registroEstado,registroGenero=registroGenero,registroRol=registroRol)
              
                    #print('usuario superAdministrador o administrador')
               # print(radioselect)
            else:
                rol2= db.execute( 'SELECT id_rol,nombre,apellido,cedula,username,email,estadoU,id_genero,id_rol FROM usuarios WHERE id_usuario = ?', (radio,) ).fetchall() 
                
                rol21=[row[0]for row in rol2]
                rol212=[row[1]for row in rol2]
                rol213=[row[2]for row in rol2]
                rol214=[row[3]for row in rol2]
                rol215=[row[4]for row in rol2]
                rol216=[row[5]for row in rol2]
                rol217=[row[6]for row in rol2]
                rol218=[row[7]for row in rol2]
                rol219=[row[8]for row in rol2]
                print(rol212[0])
                nombre=str(rol212[0])
                apellido=str(rol213[0])
                cedula=str(rol214[0])
                username=str(rol215[0])
                email=str(rol216[0])
                estado=str(rol217[0])
                genero=str(rol218[0])
                rol=str(rol219[0])

                datoestado=db.execute( 'SELECT nombre FROM estado WHERE id = ?', (estado,) ).fetchone() 
                registroEstado=str(datoestado[0])

                datogenero=db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero,) ).fetchone() 
                registroGenero=str(datogenero[0])

                datorol=db.execute( 'SELECT nombre FROM roles WHERE idRol = ?', (rol,) ).fetchone() 
                registroRol=str(datorol[0])
                
                if(str(rol21[0])=='3'):
                   
                    print('usuario final')
                    return render_template('editar_usuario3.html', nombre=nombre, apellido=apellido, cedula=cedula,username=username,email=email,registroEstado=registroEstado,registroGenero=registroGenero,registroRol=registroRol)
                else:
                     #consultar o superAdministrador o administrador
                    return render_template('editar_usuario2.html', nombre=nombre, apellido=apellido, cedula=cedula,username=username,email=email,registroEstado=registroEstado,registroGenero=registroGenero,registroRol=registroRol)
              

                

                
        #if request.method=='POST' and 'htmlsubmitbutton1' in request.POST:
         #   print('1')

        #if request.method=='POST' and 'htmlsubmitbutton2' in request.POST:
         #   print('2')
            
            #if 'newsletter_sub' in request.POST:
                 # do subscribe
                
            #elif 'newsletter_unsub' in request.POST:
                
    # do unsubscribe
            #id=request.form['radio_horizontal']
            
            #print(id)
            
            

    
        return render_template('agregar_usuario2.html')
    except:
        return render_template('agregar_usuario2.html')

@app.route("/cancelarSadministrador")
def cancelarSadministrador():
    return superUsuarios()


@app.route("/modSuper", methods=('GET', 'POST'))
def modSuper():
    try:
        if request.method == 'POST':
            db=get_db()
            rol2= db.execute( 'SELECT id_rol FROM usuarios WHERE id_usuario = ?', (newradio,) ).fetchall() 
            rol21=[row[0]for row in rol2]
            rolUser=str(rol21)

            nombre=request.form['nombre']
            apellido=request.form['apellido']
            #cedula=request.form['identificacion']
            #username=request.form['usuario']
            #email=request.form['email']
            estado=request.form['estado']
            genero=request.form['genero']
            rol=request.form['tipo_usuario']
            
            datorol=db.execute( 'SELECT idRol FROM roles WHERE nombre = ?', (rol,) ).fetchone() 
            registroRol=str(datorol[0])


            datoestado=db.execute( 'SELECT id FROM estado WHERE nombre = ?', (estado,) ).fetchone() 
            registroEstado=str(datoestado[0])

            datogenero=db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchone() 
            registroGenero=str(datogenero[0])

           
            #print(registroEstado,registroGenero,registroRol)
            if not nombre:
                error = 'Debes ingresar el nombre'
                print(error)
                flash( error )
                print(newradio)
                return superUsuarios()
            
            if not apellido:
                error = 'Debes ingresar el apellido'
                print(error)
                flash( error )
                print(newradio)
                return superUsuarios()

            sql='''UPDATE usuarios SET nombre='{}',apellido='{}',estadoU='{}',id_genero='{}',id_rol='{}' WHERE id_usuario={}'''.format(nombre,apellido,registroEstado,registroGenero,registroRol,str(newradio))
            db.execute(sql)
            db.commit()

            #print(nombre,apellido,estado,genero, rol)
            return superUsuarios()
        
           
    
        return superUsuarios()
    except:
        return superUsuarios()


@app.route("/modSuper2", methods=('GET', 'POST'))
def modSuper2():
    try:
        if request.method == 'POST':
            db=get_db()
            rol2= db.execute( 'SELECT id_rol FROM usuarios WHERE id_usuario = ?', (newradio,) ).fetchall() 
            rol21=[row[0]for row in rol2]
            rolUser=str(rol21)

            nombre=request.form['nombre']
            apellido=request.form['apellido']
            #cedula=request.form['identificacion']
            #username=request.form['usuario']
            #email=request.form['email']
            estado=request.form['estado']
            genero=request.form['genero']
           

            datoestado=db.execute( 'SELECT id FROM estado WHERE nombre = ?', (estado,) ).fetchone() 
            registroEstado=str(datoestado[0])

            datogenero=db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchone() 
            registroGenero=str(datogenero[0])
    
            if not nombre:
                error = 'Debes ingresar el nombre'
                print(error)
                flash( error )
                print(newradio)
                return superUsuarios()
            
            if not apellido:
                error = 'Debes ingresar el apellido'
                print(error)
                flash( error )
                print(newradio)
                return superUsuarios()
  
            sql='''UPDATE usuarios SET nombre='{}',apellido='{}',estadoU='{}',id_genero='{}' WHERE id_usuario={}'''.format(nombre,apellido,registroEstado,registroGenero,str(newradio))
            db.execute(sql)
            db.commit()
            return superUsuarios()

            
           
    
        return modificar1()
    except:
        return modificar1()


@app.route("/superProductos")
def superProductos():
    db=get_db()
    productos = db.execute('SELECT IdProductos,Nombre, id_categoria,id_genero,existencias,descripcion FROM productos ').fetchall()
    id=[row[0]for row in productos]
    nombre=[row[1]for row in productos]
    categoria=[row[2]for row in productos]
    genero=[row[3]for row in productos]
    cantidad=[row[4]for row in productos]
    descripcion=[row[5]for row in productos]
    num=len(id)

    valorLista=[]
    valorLista2=[]
    valorLista3=[]
    valorLista11=list()
    for i in range(num):
        nombrecategoria= db.execute( 'SELECT nombre FROM categorias WHERE IdCtegoria = ?', (categoria[i],) ).fetchall() 
        lista=[row[0]for row in nombrecategoria]
        #print(lista)
        valorLista.append(','.join(lista))
    
    for i in range(num):
        nombregenero= db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero[i],) ).fetchall() 
        lista2=[row[0]for row in nombregenero]
        #print(lista)
        valorLista2.append(','.join(lista2))

    conceptos2 = list(zip(nombre,valorLista,valorLista2,cantidad,descripcion))
   
    print(num)
    print('Esto es productos')
    return render_template('superAdministrador_productos1.html', conceptos2=conceptos2)

@app.route("/opcionesCM", methods=('GET', 'POST'))
def opcionesCM():
    try:
        if request.method == 'POST':
            db=get_db()
            radioselect= request.form['radioselect2']
            radio=str( request.form['radio_horizontal2'])
            global newradio2
            newradio2=radio

            rol2= db.execute( 'SELECT codigo,Nombre,existencias,id_genero,id_categoria,estado2,descripcion FROM productos WHERE idProductos = ?', (radio,) ).fetchall() 
            
            rol21=[row[0]for row in rol2]
            rol212=[row[1]for row in rol2]
            rol213=[row[2]for row in rol2]
            rol214=[row[3]for row in rol2]
            rol215=[row[4]for row in rol2]
            rol216=[row[5]for row in rol2]
            rol217=[row[6]for row in rol2]
            
            
            codigo=str(rol21[0])
            nombre=str(rol212[0])
            cantidad=str(rol213[0])
            genero=str(rol214[0])
            categoria=str(rol215[0])
            estado2=str(rol216[0])
            descripcion=str(rol217[0])
            
            datocategoria=db.execute( 'SELECT nombre FROM categorias WHERE idCtegoria = ?', (categoria,) ).fetchone() 
            registrocategoria=str(datocategoria[0])

            datogenero=db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero,) ).fetchone() 
            registrogenero=str(datogenero[0])

            if radioselect=='1':
                return render_template('consultar_producto_bota1.html',codigo=codigo,nombre=nombre,cantidad=cantidad,registrogenero=registrogenero,registrocategoria=registrocategoria,estado2=estado2,descripcion=descripcion,radio=radio)
            else:
                #return render_template('consultar_producto_bota1.html')
                return render_template('editar_producto_bota1.html',codigo=codigo,nombre=nombre,cantidad=cantidad,registrogenero=registrogenero,registrocategoria=registrocategoria,estado2=estado2,descripcion=descripcion,radio=radio)
           
    except:
        return superProductos()

@app.route("/modiProducto", methods=('GET', 'POST'))
def modiProducto():
    try:
        if request.method == 'POST':
            db=get_db()
            codigo=request.form['codigo']
            nombre=request.form['nombre']
            cantidad=request.form['cantidad']
            genero=request.form['genero']
            categoria=request.form['categoria']
            estado=request.form['estado']
            comentario=request.form['comentario']
            
            datogenero=db.execute( 'SELECT id FROM genero WHERE nombre = ?', (genero,) ).fetchone() 
            registrogenero=str(datogenero[0])

            datocategoria=db.execute( 'SELECT idCtegoria FROM categorias  WHERE nombre = ?', (categoria,) ).fetchone() 
            registrocategoria=str(datocategoria[0])
            
            if not codigo:
                error = 'Debes ingresar el codigo'
                print(error)
                flash( error )
                return superProductos()
            
            if not nombre:
                error = 'Debes ingresar el nombre'
                print(error)
                flash( error )
                return superProductos()
            if not cantidad:
                error = 'Debes ingresar la cantidad'
                print(error)
                flash( error )
                return superProductos()
            if not comentario:
                error = 'Debes ingresar una descripcion del producto'
                print(error)
                flash( error )
                return superProductos()
            
            sql='''UPDATE productos SET codigo='{}',Nombre='{}',existencias='{}',id_genero='{}',id_categoria='{}',estado2='{}',descripcion='{}' WHERE idProductos={}'''.format(codigo,nombre,cantidad,registrogenero,registrocategoria,estado,comentario,str(newradio2))
            db.execute(sql)
            db.commit()
            return superProductos()
            #return superProductos()
    except:
        return superProductos()

@app.route("/cerrarProductos")
def cerrarProductos():
    return superProductos()

@app.route("/calificaciones")
def calificaciones():

    db=get_db()
    productos = db.execute('SELECT IdProductos,Nombre, id_categoria,id_genero,existencias,descripcion,calificacion2 FROM productos ').fetchall()
    id=[row[0]for row in productos]
    nombre=[row[1]for row in productos]
    categoria=[row[2]for row in productos]
    genero=[row[3]for row in productos]
    cantidad=[row[4]for row in productos]
    descripcion=[row[5]for row in productos]
    calificacion2=[row[6]for row in productos]
    num=len(id)

    valorLista=[]
    valorLista2=[]
    valorLista3=[]
    valorLista11=list()
    for i in range(num):
        nombrecategoria= db.execute( 'SELECT nombre FROM categorias WHERE IdCtegoria = ?', (categoria[i],) ).fetchall() 
        lista=[row[0]for row in nombrecategoria]
        #print(lista)
        valorLista.append(','.join(lista))
    
    for i in range(num):
        nombregenero= db.execute( 'SELECT nombre FROM genero WHERE id = ?', (genero[i],) ).fetchall() 
        lista2=[row[0]for row in nombregenero]
        #print(lista)
        valorLista2.append(','.join(lista2))

    conceptos2 = list(zip(calificacion2,nombre,valorLista,valorLista2,cantidad,descripcion))
    data=''
    print(num)
    print('Esto es productos')
    return render_template('superAdministrador_calificaciones1.html', conceptos2=conceptos2,calificacion2=calificacion2)

@app.route("/inicio1")
def inicio1():
    return render_template('inicio1.html')

@app.route("/inicio2")
def inicio2():
    return render_template('inicio2.html')

@app.route("/inicio3")
def inicio3():
    return render_template('inicio3.html')

@app.route("/inicio4")
def inicio4():
    return render_template('inicio4.html')
@app.route("/inicio5")
def inicio5():
    return render_template('inicio5.html')

@app.route("/inicio6")
def inicio6():
    return render_template('inicio6.html')

@app.route("/inicio7")
def inicio7():
    return render_template('inicio7.html')

@app.route("/inicio8")
def inicio8():
    return render_template('inicio8.html')

@app.route("/inicio9")
def inicio9():
    return render_template('inicio9.html')

@app.route("/inicio10")
def inicio10():
    return render_template('inicio10.html')

@app.route("/inicio11")
def inicio11():
    return render_template('inicio11.html')

@app.route("/inicio12")
def inicio12():
    return render_template('inicio12.html')

@app.route("/ofertas")
def ofertas():
    return render_template('inicio.html')

@app.route("/compra2")
def compra2():
    db=get_db()
    valor='3'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)


@app.route("/compra1")
def compra1():
    db=get_db()
    valor='1'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)


@app.route("/compra12")
def compra12():
    db=get_db()
    valor='12'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)

@app.route("/compra6")
def compra6():
    db=get_db()
    valor='6'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)


@app.route("/compra9")
def compra9():
    db=get_db()
    valor='9'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)

@app.route("/compra15")
def compra15():
    db=get_db()
    valor='15'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)

@app.route("/compra18")
def compra18():
    db=get_db()
    valor='18'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)

@app.route("/compra21")
def compra21():
    db=get_db()
    valor='21'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)

@app.route("/compra30")
def compra30():
    db=get_db()
    valor='30'
    nombre=db.execute( 'SELECT Nombre FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registronombre=str(nombre[0])

    idcolor=db.execute( 'SELECT color2 FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registroidcolor=str(idcolor[0])

    color=db.execute( 'SELECT nombre FROM color  WHERE idColor = ?', (registroidcolor,) ).fetchone() 
    registrocolor=str(color[0])

    descripcion=db.execute( 'SELECT descripcion FROM productos  WHERE IdProductos = ?', (valor,) ).fetchone() 
    registrodescripcion=str(descripcion[0])

    return render_template('compra.html', registronombre=registronombre, valor=valor, registrocolor=registrocolor,registrodescripcion=registrodescripcion)



if __name__ == '__main__':
    app.run(debug=True)