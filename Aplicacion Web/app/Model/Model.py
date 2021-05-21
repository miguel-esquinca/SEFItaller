import sys
sys.path.append(".")
from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

#MODELO DE LA BASE DE DATOS



class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))


    Venta = relationship("Venta")

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(50))
    rfc = db.Column(db.String(50))
    domicilio = db.Column(db.String(50))
    telefono = db.Column(db.Integer())


    Venta = relationship("Venta")


class Venta(db.Model):
    __tablename__ = 'Venta'
    id_venta = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(50))
    nombre_servicio  = db.Column(db.String(50))
    cantidad_producto = db.Column(db.Integer())
    precio_pu = db.Column(db.Integer())
    fk_usuario = Column(Integer, ForeignKey('Usuario.id'))
    fk_cliente = Column(Integer, ForeignKey('Cliente.id_cliente'))



db.create_all()