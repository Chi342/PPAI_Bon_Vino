#!/usr/bin/python
#-*- coding: utf-8 -*-

class Varietal:
    def __init__(self, descripción, porcentajeComposición):
        """
        Constructor de la clase Varietal.

        Parámetros:
        - descripción (str): La descripción del varietal.
        - porcentajeComposición (float): El porcentaje de composición del varietal.
        """
        self.descripción = descripción
        self.porcentajeComposición = porcentajeComposición

    def getDescripcion(self):
        """
        Devuelve la descripción del varietal.

        Retorna:
        - str: La descripción del varietal.
        """
        return self.descripción
