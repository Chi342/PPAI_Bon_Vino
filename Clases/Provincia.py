#!/usr/bin/python
#-*- coding: utf-8 -*-

class Provincia:
    def __init__(self, nombre, pais):
        """
        Constructor de la clase Provincia.

        Parámetros:
        - nombre (str): El nombre de la provincia.
        - pais (Pais): El objeto Pais al que pertenece la provincia.
        """
        self.nombre = nombre
        self.pais = pais

    def obtenerPais(self):
        """
        Obtiene el nombre del país al que pertenece la provincia.

        Retorna:
        - str: El nombre del país.
        """
        return self.pais.getNombre()
