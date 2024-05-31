#!/usr/bin/python
#-*- coding: utf-8 -*-

class Pais:
    def __init__(self, nombre):
        """
        Constructor de la clase Pais.

        Parámetros:
        - nombre (str): El nombre del país.
        """
        self.nombre = nombre

    def getNombre(self):
        """
        Método para obtener el nombre del país.

        Retorna:
        - str: El nombre del país.
        """
        return self.nombre
