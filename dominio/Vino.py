#!/usr/bin/python
#-*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Vino(Base):
    __tablename__ = 'Vino'

    id = Column(Integer, primary_key=True, autoincrement=True)
    añada = Column(Integer, nullable=True)
    fechaActualizacion = Column(DateTime, nullable=True)
    imagenEtiqueta = Column(Integer, nullable=True)
    nombre = Column(String(50), nullable=True)
    notaDeCataBodega = Column(Integer, nullable=True)
    precioARS = Column(Numeric(18, 0), nullable=True)

    def tenesResenasDeTipoEnPeriodo(self, tipo: str, inicio: datetime, fin: datetime) -> bool:
        # Implementation goes here
        pass

    def getNombre(self) -> str:
        return self.nombre

    def getPrecio(self) -> float:
        return self.precioARS

    def buscarInfoBodega(self) -> dict:
        # Implementation goes here
        pass

    def buscarVarietal(self) -> str:
        # Implementation goes here
        pass

    def calcularPuntajeDeSommelierEnPeriodo(self, inicio: datetime, fin: datetime) -> float:
        # Implementation goes here
        pass

    def calcularPuntajePromedio(self) -> float:
        # Implementation goes here
        pass

# Connection setup using Windows Authentication
DATABASE_URI = (
    'mssql+pyodbc:///?odbc_connect='
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAIN;'
    'DATABASE=Bon_vino;'
    'Trusted_Connection=yes;'
)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

