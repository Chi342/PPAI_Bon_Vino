#!/usr/bin/python
#-*- coding: utf-8 -*-

class Provincia:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

    def obtenerPais(self, ):
        return self.pais.getNombre()


