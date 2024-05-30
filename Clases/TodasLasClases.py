#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from Bodega import *
import Pais
import Provincia
import RegionVitivinicola
sys.path.append('C:/Users/Roberto/source/repos/robertoutn/PPAI_BON_VINO/')
import datetime
import os
import random
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, DECIMAL, ForeignKey, Identity, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Vino import Vino
from database import Session
from Reseña import Reseña

Base = declarative_base()

class DTOBodega(Base):
    __tablename__ = 'Bodega'
    id = Column(Integer, primary_key=True, nullable=False)
    coordenadasUbicacion = Column(String(20), nullable=True)
    descripcion = Column(Text, nullable=False)
    historia = Column(Text, nullable=True)
    nombre = Column(String(50), nullable=False)
    periodoActualizacion = Column(Integer, nullable=True)
    regionVitivinicola = Column(Integer, ForeignKey('RegionVitivinicola.id'), nullable=True)

#    regiones = relationship("RegionVitivinicola", back_populates="bodegas")
#    vinos = relationship("Vino", back_populates="bodegas")

class DTOPais(Base):
    __tablename__ = 'Pais'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)

#    provincias = relationship("Provincia", back_populates="paises")

class DTOProvincia(Base):
    __tablename__ = 'Provincia'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    pais = Column(Integer, ForeignKey('Pais.id'), nullable=False)

#    paises = relationship("Pais", back_populates="provincias")
#    regiones = relationship("RegionVitivinicola", back_populates="provincias")

class DTORegionVitivinicola(Base):
    __tablename__ = 'RegionVitivinicola'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    provincia = Column(Integer, ForeignKey('Provincia.id'), nullable=False)

#    provincias = relationship("Provincia", back_populates="regiones")
#    bodegas = relationship("Bodega", back_populates="regiones")

class DTOResenia(Base):
    __tablename__ = 'Resenia'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    comentario = Column(Text, nullable=True)
    premium = Column(Boolean, nullable=False)
    fechaResenia = Column(DateTime, nullable=True)
    puntaje = Column(DECIMAL(5, 2), nullable=True)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

#    vino = relationship("Vino", back_populates="resenias")

class DTOVarietal(Base):
    __tablename__ = 'Varietal'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    porcentajeComposicion = Column(DECIMAL(5, 2), nullable=False)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

#    vino = relationship("Vino", back_populates="varietales")


class DTOVino(Base):
    __tablename__ = 'Vino'
    idVino = Column(Integer, primary_key=True, nullable=False)
    aniada = Column(Integer, nullable=True)
    fechaActualizacion = Column(DateTime, nullable=True)
    imagenEtiqueta = Column(Integer, nullable=True)
    nombre = Column(String(50), nullable=True)
    notaDeCataBodega = Column(Integer, nullable=True)
    precioARS = Column(DECIMAL(10, 2), nullable=True)
    bodega = Column(Integer, nullable=False)
    #bodega = Column(Integer, ForeignKey('Bodega.id'), nullable=False)  # Update column name here
    
#    bodegas = relationship("Bodega", back_populates="vinos")
#    resenias = relationship("Resenia", back_populates="vino")
#    varietales = relationship("Varietal", back_populates="vino")
    
    @staticmethod
    def consultar_vinos(lista_vinos):
        session = Session()
        vinos = session.query(DTOVino).all()
        lista_bodegas = []  # Define the "lista_bodegas" variable
        bodegas = session.query(DTOBodega).all()
        for b in bodegas:
            idBodega = b.id
            coordenadasUbicacion = b.coordenadasUbicacion
            descripcion = b.descripcion
            historia = b.historia
            nombre = b.nombre
            periodoActualizacion = b.periodoActualizacion
            regionVitivinicola = session.query(DTORegionVitivinicola).filter(DTORegionVitivinicola.id == b.regionVitivinicola).first()
            regionVitivinicola = RegionVitivinicola(regionVitivinicola.nombre, regionVitivinicola.descripcion, regionVitivinicola.provincia)
            lista_bodegas.append(Bodega(coordenadasUbicacion, descripcion, historia, nombre, periodoActualizacion, regionVitivinicola))
        session.close()
        
        paises = session.query(DTOPais).all()
        lista_paises = []
        for p in paises:
            idPais = p.id
            nombre = p.nombre
            lista_paises.append(Pais(nombre))
        session.close()
        
        def crear_lista_regiones():
            session = Session()
            regiones = session.query(DTORegionVitivinicola).all()
            lista_regiones = []
            for r in regiones:
                idRegion = r.id
                nombre = r.nombre
                descripcion = r.descripcion
                provincia = session.query(DTOProvincia).filter(DTOProvincia.id == r.provincia).first()
                provincia = Provincia(provincia.nombre, provincia.pais)
                lista_regiones.append(RegionVitivinicola(nombre, descripcion, provincia))
            session.close()
            return lista_regiones
        
        def crear_lista_resenias(i):
            # Add your implementation here
            resenias = session.query(DTOResenia).filter(DTOResenia.idVino == vinos[i].idVino).all()
            resenia = []
            for r in resenias:
                idResenia = r.id
                comentario = r.comentario
                premium = r.premium
                fechaResenia = r.fechaResenia
                puntaje = r.puntaje
                idVino = r.idVino
                resenia.append(Reseña(comentario, premium, fechaResenia.year, fechaResenia.month, fechaResenia.day, puntaje))
#                print("Vino: ", idVino, "Reseña: ", idResenia, "Comentario: ", comentario, "Premium: ", premium, "Fecha: ", fechaResenia, "Puntaje: ", puntaje)
            return resenia

        etiquetas = os.listdir('Clases/extras/etiquetas')
        for i in range(len(vinos)):
            idVino = i
            añada = vinos[i].aniada
            fechaActualizacion = vinos[i].fechaActualizacion
            imagenEtiqueta = random.choice(etiquetas)
            nombre = vinos[i].nombre
            notaDeCataBodega=vinos[i].notaDeCataBodega
            precioARS = vinos[i].precioARS
            resenias = crear_lista_resenias(i)
            nuevo_vino = Vino(añada, fechaActualizacion,imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, resenias)
            lista_vinos.append(nuevo_vino)
            # for vino in lista_vinos:
            #     print()
            #     print("Vino:", vino.nombre)
            #     print("Añada:", vino.añada)
            #     print("Fecha de Actualización:", vino.fechaActualización)
            #     print("Imagen de Etiqueta:", vino.imagenEtiqueta)
            #     print("Nota de Cata de Bodega:", vino.notaDeCataBodega)
            #     print("Precio en ARS:", vino.precioARS)
            #     print("Bodega:", vino.bodega)
            #     for resenia in vino.reseñas:
            #         print("Reseña:")
            #         print("Comentario:", resenia.comentario)
            #         print("es premium:",resenia.esPremium)
            #         print("Fecha de Reseña:", resenia.fechaReseña)
            #         print("Puntaje:", resenia.puntaje)
            
        return lista_vinos
