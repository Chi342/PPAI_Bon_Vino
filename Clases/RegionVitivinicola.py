#!/usr/bin/python
#-*- coding: utf-8 -*-

class RegionVitivinicola:
    def __init__(self, descripción, nombre, provincia):
        """
        Constructor de la clase RegionVitivinicola.

        Parámetros:
        - descripción (str): La descripción de la región vitivinícola.
        - nombre (str): El nombre de la región vitivinícola.
        - provincia (Provincia): La provincia a la que pertenece la región vitivinícola.
        """
        self.descripción = descripción
        self.nombre = nombre
        self.provincia = provincia

    def getNombre(self):
        """
        Método para obtener el nombre de la región vitivinícola.

        Retorna:
        - str: El nombre de la región vitivinícola.
        """
        return self.nombre

    def obtenerPais(self):
        """
        Método para obtener el país al que pertenece la región vitivinícola.

        Retorna:
        - str: El país al que pertenece la región vitivinícola.
        """
        return self.provincia.obtenerPais()
