#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
se deben ejecutar los siguientes comandos desde una consola (cmd o powershell): 
pip install flask
pip install sqlalchemy
pip install flask-sqlalchemy
pip install mssql
"""

# repositorio/queryAll.py
import sys
import os
import connection

# Añadir el directorio base al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dominio.Vino import Vino
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crea una sesión
Session = sessionmaker(bind=connection.engine)
session = Session()

# Obtiene todos los objetos mapeados de la tabla Vino
vinos = session.query(Vino).all()

# Itera sobre los objetos mapeados y muestra sus atributos
for vino in vinos:
    print("ID:", vino.id)
    print("Añada:", vino.añada)
    print("Fecha de actualización:", vino.fechaActualizacion)
    print("Imagen de etiqueta:", vino.imagenEtiqueta)
    print("Nombre:", vino.nombre)
    print("Nota de cata de bodega:", vino.notaDeCataBodega)
    print("Precio en ARS:", vino.precioARS)
    print()
