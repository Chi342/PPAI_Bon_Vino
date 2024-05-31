#!/usr/bin/python
#-*- coding: utf-8 -*-

class Provincia:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def obtenerPais(self, ):
        return self.pais.getNombre()

    def getNombre(self, ):
        return self.nombre

    def setNombre(self, value):
        self.nombre = value

