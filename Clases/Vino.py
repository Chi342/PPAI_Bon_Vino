#!/usr/bin/python
#-*- coding: utf-8 -*-

class Vino:
    def __init__(self, añada, fechaActualizacion, nombre, nota, precio, bodega, varietal):
        self.añada = añada
        self.fechaActualización = fechaActualizacion
        self.imagenEtiqueta = None
        self.nombre = nombre
        self.notaDeCataBodega = nota
        self.precioARS = precio
        self.bodega = bodega
        self.reseña = []
        self.varietal = varietal

    def tenesResenasDeTipoEnPeriodo(self, ):
        for i in range(len(self.reseña)):
            enPeriodo = self.reseña[i].sosDePeriodo()
            esDeSommelier = self.reseña[i].sosDeSommelier()

    def buscarInfoBodega(self, ):
        nombreBodega = self.bodega.getNombre()
        regionYPais = self.bodega.obtenerRegionYPais()

    def buscarVarietal(self, ):
        varietal = self.varietal.getDescripción()

    def calcularPuntajeDeSommelierEnPeriodo(self, ):
        puntajes = []
        for i in range(len(self.reseña)):
            enPeriodo = self.reseña[i].sosDePeriodo()
            esDeSommelier = self.reseña[i].sosDeSommelier()
            if enPeriodo and esDeSommelier:
                puntajes.append(self.reseña[i].getPuntaje)
        promPunt = self.calcularPuntajePromedio(puntajes)
        return promPunt

    def calcularPuntajePromedio(self, puntajes):
        sumPuntajes = 0
        cantPuntajes = len(puntajes)
        for i in range(cantPuntajes):
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



