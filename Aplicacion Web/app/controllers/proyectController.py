import random
from flask import Flask, request, redirect, url_for, flash,Response, stream_with_context,make_response
from flask import session as sesion
from flask import Blueprint, render_template


import numpy as np
from app import db
from app import app

import pdfkit

from jinja2 import Environment, FileSystemLoader
import time

import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from app.Model.Model import Cliente
from app.Model.Model import Usuario
from app.Model.Model import Venta


engine = create_engine('mysql+pymysql://root:@localhost/sefi')
Session = sessionmaker(bind=engine)
session = Session()



#SEGUIR CON LA LIBRERIA LOGIN

#DEFINICIÓN DE TODAS LAS FUNCIONES
sefi_Route = Blueprint('sefi',__name__)

class Loging():
    #DEFINICION DE LA RUTA RAIZ DE LOGIN
    @sefi_Route.route('/',methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['correo']
            password = request.form['contraseña']
            print(email)
            print(password)
            user = session.query(Usuario.id).filter_by(correo=email,contraseña=password).scalar()
            print(user)
            if user:
                sesion['user'] = user
                return redirect('/inicio')
            if not user:
                flash('Usuario o contraseña incorrecta')
                return render_template('index.html')
        return render_template('index.html')

    @sefi_Route.route('/inicio')
    def inicio():
        if sesion['user']:
            facturas = session.query(Venta.id_venta,Venta.nombre_producto,Venta.nombre_servicio,Venta.cantidad_producto,
            Venta.precio_pu,Cliente.nombre_cliente,Cliente.rfc,Cliente.telefono).join(Cliente).all()
            
            return render_template('inicio.html',facturas1 = facturas)
                
        return redirect('/')

    @sefi_Route.route('/usuario',methods=['GET','POST'])
    def usuario():
        if request.method == 'POST':
            nombre = request.form['nombre']
            correo = request.form['correo']
            contraseña = request.form['contraseña']
            
            NewUser = Usuario(nombre=nombre,correo=correo,contraseña=contraseña)
            session.add( NewUser)
            session.commit()
            flash('Agregado correctamente')
            return redirect('/usuario')
        if sesion['user']:  
            return render_template('usuario.html')          
        return redirect('/')

    @sefi_Route.route('/cliente',methods=['GET','POST'])
    def cliente():
        if request.method == 'POST':
            nombre = request.form['nombre']
            rfc = request.form['rfc']
            domicilio = request.form['domicilio']
            telefono = request.form['telefono']
            NewClient = Cliente(nombre_cliente=nombre,rfc=rfc,domicilio=domicilio,telefono=telefono)
            session.add(NewClient)
            session.commit()
            flash('Agregado correctamente')
            return redirect('/cliente')
        if sesion['user']:  
            return render_template('cliente.html')          
        return redirect('/')

    @sefi_Route.route('/facturar',methods=['GET','POST'])
    def facturar():
        if request.method == 'POST':
            nombreP = request.form['nombre']
            servicio = request.form['servicio']
            cantidad = request.form['cantidad']
            precio = request.form['precio']
            id_cliente = request.form['nombre_cliente']
            NewFactura = Venta(nombre_producto=nombreP,nombre_servicio=servicio,cantidad_producto=cantidad,precio_pu=precio,fk_usuario=sesion['user'],fk_cliente=id_cliente)
            session.add(NewFactura)
            session.commit()
            flash('Agregado correctamente')
            return redirect('/facturar')
        if sesion['user']:  
            Clientes1 = session.query(Cliente.id_cliente,Cliente.nombre_cliente).all()
            print(Clientes1)
            return render_template('facturar.html',Clientes = Clientes1)          
        return redirect('/')

    @sefi_Route.route('/pdf/<int:id>')
    def pdf(id):
        pdfid= id
        impPDFFactura = session.query(Venta.id_venta,Venta.nombre_producto,Venta.nombre_servicio,Venta.cantidad_producto,
            Venta.precio_pu,Cliente.nombre_cliente,Cliente.rfc,Cliente.telefono).filter(Venta.id_venta==pdfid).join(Cliente).first()
        
        env = Environment(loader=FileSystemLoader("./app/templates/"))
        template = env.get_template("pdf.html")
        config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        print(impPDFFactura[0])
        id2=impPDFFactura[0]
        nproducto = impPDFFactura[1]
        nservicio = impPDFFactura[2]
        cantidad = impPDFFactura[3]
        precio = impPDFFactura[4]
        nombreC = impPDFFactura[5]
        rfc = impPDFFactura[6]
        telefono = impPDFFactura[7]
        usuario = {
            'id':id2,
            'nproducto':nproducto,
            'nservicio':nservicio,
            'cantidad':cantidad,
            'precio':precio,
            'nombreC':nombreC,
            'rfc':rfc,
            'telefono':telefono
        }

        html = template.render(usuario)
        f = open('nuevo_pdf.html','w')
        f.write(html)
        f.close()

        aleatorio = random.randrange(10000)
        pdfkit.from_file('nuevo_pdf.html','nuevo'+str(aleatorio) +'.pdf',configuration=config)

        os.remove('nuevo_pdf.html')

        return redirect('/inicio')








