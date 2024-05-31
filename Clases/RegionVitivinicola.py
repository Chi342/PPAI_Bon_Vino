#!/usr/bin/python
#-*- coding: utf-8 -*-

class RegionVitivinicola:
    def __init__(self, descripción, nombre, provincia):
        self.descripción = descripción
        self.nombre = nombre
        self.provincia = provincia

    def getNombre(self, ):
        return self.nombre

    def obtenerPais(self, ):
        return self.provincia.obtenerPais()


