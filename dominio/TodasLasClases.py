#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('C:/Users/Roberto/source/repos/robertoutn/PPAI_BON_VINO/')
import datetime
import os
import random
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, DECIMAL, ForeignKey, Identity, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Clases.Vino import Vino
from database import Session

Base = declarative_base()
"""
class DTOBodega(Base):
    __tablename__ = 'Bodega'
    id = Column(Integer, primary_key=True, nullable=False)
    coordenadasUbicacion = Column(String(20), nullable=True)
    descripcion = Column(Text, nullable=False)
    historia = Column(Text, nullable=True)
    nombre = Column(String(50), nullable=False)
    periodoActualizacion = Column(Integer, nullable=True)
    regionVitivinicola = Column(Integer, ForeignKey('RegionVitivinicola.id'), nullable=True)

    regiones = relationship("RegionVitivinicola", back_populates="bodegas")
    vinos = relationship("Vino", back_populates="bodegas")

class DTOPais(Base):
    __tablename__ = 'Pais'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)

    provincias = relationship("Provincia", back_populates="paises")

class DTOProvincia(Base):
    __tablename__ = 'Provincia'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    pais = Column(Integer, ForeignKey('Pais.id'), nullable=False)

    paises = relationship("Pais", back_populates="provincias")
    regiones = relationship("RegionVitivinicola", back_populates="provincias")

class DTORegionVitivinicola(Base):
    __tablename__ = 'RegionVitivinicola'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    provincia = Column(Integer, ForeignKey('Provincia.id'), nullable=False)

    provincias = relationship("Provincia", back_populates="regiones")
    bodegas = relationship("Bodega", back_populates="regiones")

class DTOResenia(Base):
    __tablename__ = 'Resenia'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    comentario = Column(Text, nullable=True)
    premium = Column(Boolean, nullable=False)
    fechaResenia = Column(DateTime, nullable=True)
    puntaje = Column(DECIMAL(5, 2), nullable=True)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

    vino = relationship("Vino", back_populates="resenias")

class DTOVarietal(Base):
    __tablename__ = 'Varietal'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    porcentajeComposicion = Column(DECIMAL(5, 2), nullable=False)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

    vino = relationship("Vino", back_populates="varietales")
"""

class DTOVino(Base):
    __tablename__ = 'Vino'
    idVino = Column(Integer, primary_key=True, nullable=False)
    aniada = Column(Integer, nullable=True)
    fechaActualizacion = Column(DateTime, nullable=True)
    imagenEtiqueta = Column(Integer, nullable=True)
    nombre = Column(String(50), nullable=True)
    notaDeCataBodega = Column(Integer, nullable=True)
    precioARS = Column(DECIMAL(10, 2), nullable=True)
    bodega = Column(Integer, ForeignKey('Bodega.id'), nullable=False)  # Update column name here

#    bodegas = relationship("Bodega", back_populates="vinos")
#    resenias = relationship("Resenia", back_populates="vino")
#    varietales = relationship("Varietal", back_populates="vino")
    
    #@staticmethod
    #def consultar_vinos():
    #    session = Session()
    #    vinos = session.query(Vino).all()
    #    session.close()
    #    return vinos
    def crear_lista_bodegas():
        bodegas = []
        for i in range(10):
            pass
        return bodegas

    def crear_lista_varietal():
        varietales = []
        for i in range(10):
            pass
        return varietales


    @staticmethod
    def consultar_vinos(lista_vinos):
        session = Session()
        vinos = session.query(DTOVino).all()
        session.close()
        
        etiquetas = os.listdir('dominio/extras/etiquetas')
        bodega = []#crear_lista_bodegas()
        varietal = []#crear_lista_varietales()
        for i in range(len(vinos)):
            idVino = i + 100
            añada = vinos[i].aniada
            fechaActualizacion = vinos[i].fechaActualizacion
            imagenEtiqueta = random.choice(etiquetas)
            nombre = vinos[i].nombre
            notaDeCataBodega=vinos[i].notaDeCataBodega
            precioARS = vinos[i].precioARS

            nuevo_vino = Vino(añada, fechaActualizacion,imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, varietal)
            lista_vinos.append(nuevo_vino)
        return lista_vinos
