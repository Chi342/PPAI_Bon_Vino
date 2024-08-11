#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
# sys.path.append('/mnt/linux/repositories/PPAI_BON_VINO/Clases')

from Clases.Bodega import Bodega
from Clases.Pais import Pais
from Clases.Provincia import Provincia
from Clases.RegionVitivinicola import RegionVitivinicola
from Clases.Varietal import Varietal
import datetime
import os
import random
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, DECIMAL, ForeignKey, Identity, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from Clases.Vino import Vino
from Clases.database import Session
from Clases.Reseña import Reseña

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
        lista_bodegas = []
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
        
        session = Session()
        bodegas = session.query(DTOBodega).all()
        lista_bodegas = []
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
            return resenia

        def crear_lista_varietales(i):
            # Add your implementation here
            varietales = session.query(DTOVarietal).filter(DTOVarietal.idVino == vinos[i].idVino).all()
            lista_varietales = []
            for v in varietales:
                descripcion = v.descripcion
                porcentajeComposicion = v.porcentajeComposicion
                lista_varietales.append(Varietal(descripcion, porcentajeComposicion))
            return lista_varietales

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
            varietales = crear_lista_varietales(i)
            
            bodega = session.query(DTOBodega).filter(DTOBodega.id == vinos[i].bodega).first()
            
            regionVitivinicola = session.query(DTORegionVitivinicola).filter(DTORegionVitivinicola.id == bodega.regionVitivinicola).first()
            
            provincia = session.query(DTOProvincia).filter(DTOProvincia.id == regionVitivinicola.provincia).first()
            pais = session.query(DTOPais).filter(DTOPais.id == provincia.pais).first()
            pais = Pais(pais.nombre)
            provincia = Provincia(provincia.nombre, pais)
            regionVitivinicola = RegionVitivinicola(regionVitivinicola.nombre, regionVitivinicola.descripcion, provincia)

            bodega = Bodega(bodega.coordenadasUbicacion, bodega.descripcion, bodega.historia, bodega.nombre, bodega.periodoActualizacion, regionVitivinicola)
            nuevo_vino = Vino(añada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, resenias, varietales)
            lista_vinos.append(nuevo_vino)
            
        return lista_vinos
