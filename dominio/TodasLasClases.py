#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, DECIMAL, ForeignKey, Identity, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import urllib

Base = declarative_base()

class Bodega(Base):
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

class Pais(Base):
    __tablename__ = 'Pais'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)

    provincias = relationship("Provincia", back_populates="paises")

class Provincia(Base):
    __tablename__ = 'Provincia'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    pais = Column(Integer, ForeignKey('Pais.id'), nullable=False)

    paises = relationship("Pais", back_populates="provincias")
    regiones = relationship("RegionVitivinicola", back_populates="provincias")

class RegionVitivinicola(Base):
    __tablename__ = 'RegionVitivinicola'
    id = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    provincia = Column(Integer, ForeignKey('Provincia.id'), nullable=False)

    provincias = relationship("Provincia", back_populates="regiones")
    bodegas = relationship("Bodega", back_populates="regiones")

class Resenia(Base):
    __tablename__ = 'Resenia'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    comentario = Column(Text, nullable=True)
    premium = Column(Boolean, nullable=False)
    fechaResenia = Column(DateTime, nullable=True)
    puntaje = Column(DECIMAL(5, 2), nullable=True)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

    vino = relationship("Vino", back_populates="resenias")

class Varietal(Base):
    __tablename__ = 'Varietal'
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    porcentajeComposicion = Column(DECIMAL(5, 2), nullable=False)
    idVino = Column(Integer, ForeignKey('Vino.idVino'), nullable=False)

    vino = relationship("Vino", back_populates="varietales")

class Vino(Base):
    __tablename__ = 'Vino'
    idVino = Column(Integer, primary_key=True, nullable=False)
    aniada = Column(Integer, nullable=True)
    fechaActualizacion = Column(DateTime, nullable=True)
    imagenEtiqueta = Column(Integer, nullable=True)
    nombre = Column(String(50), nullable=True)
    notaDeCataBodega = Column(Integer, nullable=True)
    precioARS = Column(DECIMAL(10, 2), nullable=True)
    bodega = Column(Integer, ForeignKey('Bodega.id'), nullable=False)  # Update column name here

    bodegas = relationship("Bodega", back_populates="vinos")
    resenias = relationship("Resenia", back_populates="vino")
    varietales = relationship("Varietal", back_populates="vino")


