from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, MetaData, Table,DateTime, Date , ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists, select
import datetime
import pandas as pd
from sqlalchemy.sql import func


engine = create_engine('mysql+pymysql://root:@localhost/sefi')
Session = sessionmaker(bind=engine)
session = Session()

#MODELO DE LA BASE DE DATOS
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    correo = Column(String(50))
    contraseña = Column(String(50))


    Venta = relationship("Venta")

class Cliente(Base):
    __tablename__ = 'Cliente'
    id_cliente = Column(Integer, primary_key=True)
    nombre_cliente = Column(String(50))
    rfc = Column(String(50))
    domicilio = Column(String(50))
    telefono = Column(Integer())


    Venta = relationship("Venta")


class Venta(Base):
    __tablename__ = 'Venta'
    id_venta = Column(Integer, primary_key=True)
    nombre_producto = Column(String(50))
    nombre_servicio  = Column(String(50))
    cantidad_producto = Column(Integer())
    precio_pu = Column(Integer())
    fk_usuario = Column(Integer, ForeignKey('Usuario.id'))
    fk_cliente = Column(Integer, ForeignKey('Cliente.id_cliente'))



