#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bodega:
    def __init__(self):
        self.coordenadasUbicación = None
        self.descripción = None
        self.historia = None
        self.nombre = None
        self.periodoActualización = None
        self.region = None

    def getNombre(self, ):
        pass

    def obtenerRegionYPais(self, ):
        region = self.region.getNombre()
        pais = self.region.obtenerPais()
        return [region, pais]

    def getCoordenadasUbicación(self, ):
        pass

    def setCoordenadasUbicación(self, value):
        pass

    def getDescripción(self, ):
        pass

    def setDescripción(self, value):
        pass

    def getHistoria(self, ):
        pass

    def setHistoria(self, value):
        pass

    def getNombre(self, ):
        pass

    def setNombre(self, value):
        pass

    def getPeriodoActualización(self, ):
        pass

    def setPeriodoActualización(self, value):
        pass

