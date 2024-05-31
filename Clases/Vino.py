#!/usr/bin/python
#-*- coding: utf-8 -*-

from Reseña import Reseña


class Vino:
    def __init__(self, añada, fechaActualizacion, imagen, nombre, nota, precio, bodega, reseñas, varietales):
        self.añada = añada
        self.fechaActualización = fechaActualizacion
        self.imagenEtiqueta = imagen
        self.nombre = nombre
        self.notaDeCataBodega = nota
        self.precioARS = precio
        self.bodega = bodega
        self.reseñas = reseñas
        self.varietales = varietales

    def tenesResenasDeTipoEnPeriodo(self,fechaDesde, fechaHasta):
        vinosQueCumplenConFiltros = []  # Define the variable here
        for i in range(len(self.reseñas)):
            enPeriodo = self.reseñas[i].sosDePeriodo(fechaDesde, fechaHasta)
            sosDeTipo = self.reseñas[i].sosDeSommelier()
            if enPeriodo and sosDeTipo:
                vinosQueCumplenConFiltros.append(self.reseñas[i])
        return vinosQueCumplenConFiltros

    def buscarInfoBodega(self, ):
        nombreBodega = self.bodega.getNombre()
        region,pais = self.bodega.obtenerRegionYPais()
        return nombreBodega, region, pais

    def buscarVarietal(self, ):
        varietales = ""
        for i in self.varietales:
            varietales += str(i.getDescripcion()) + " "
        return varietales

    def calcularPuntajeDeSommelierEnPeriodo(self, fechaDesde, fechaHasta):
        puntajes = []
        for i in range(len(self.reseñas)):
            enPeriodo = self.reseñas[i].sosDePeriodo(fechaDesde, fechaHasta)
            esDeSommelier = self.reseñas[i].sosDeSommelier()
            if enPeriodo and esDeSommelier:
                puntajes.append(self.reseñas[i].getPuntaje())
        promPunt = self.calcularPuntajePromedio(puntajes)
        return promPunt

    def calcularPuntajePromedio(self, puntajes):
        sumPuntajes = 0
        cantPuntajes = len(puntajes)
        for i in range(cantPuntajes):
            if puntajes[i] is not None:
                sumPuntajes += puntajes[i]
        if cantPuntajes != 0:
            promPuntajes = sumPuntajes / cantPuntajes
        else:
            promPuntajes = 0
        return promPuntajes
    
    def getAñada(self, ):
        return self.añada

    def setAñada(self, value):
        self.añada = value

    def getFechaActualización(self, ):
        return self.fechaActualización

    def setFechaActualización(self, value):
        self.fechaActualización = value

    def getImagenEtiqueta(self, ):
        return self.imagenEtiqueta


    def setImagenEtiqueta(self, value):
        self.imagenEtiqueta = value

    def getNombre(self, ):
        return self.nombre

    def setNombre(self, value):
        self.nombre = value

    def getNotaDeCataBodega(self, ):
        return self.notaDeCataBodega

    def setNotaDeCataBodega(self, value):
        self.notaDeCataBodega = value

    def getPrecioARS(self, ):
        return self.precioARS

    def setPrecioARS(self, value):
        self.precioARS = value

    def conocerReseña(self, ):
        return self.precioARS

    def agregarReseña(self, value):
        self.reseña.append(value)



