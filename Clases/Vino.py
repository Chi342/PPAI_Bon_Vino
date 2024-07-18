#!/usr/bin/python
#-*- coding: utf-8 -*-
from Clases.Reseña import Reseña
class Vino:
    def __init__(self, añada, fechaActualizacion, imagen, nombre, nota, precio, bodega, reseñas, varietales):
        """
        Constructor de la clase Vino.

        Parámetros:
        - añada (int): Año de producción del vino.
        - fechaActualizacion (str): Fecha de la última actualización del vino.
        - imagen (str): Ruta de la imagen de la etiqueta del vino.
        - nombre (str): Nombre del vino.
        - nota (float): Nota de cata otorgada por la bodega.
        - precio (float): Precio del vino en ARS.
        - bodega (Bodega): Objeto de la clase Bodega que representa la bodega del vino.
        - reseñas (list): Lista de objetos de la clase Reseña que representan las reseñas del vino.
        - varietales (list): Lista de objetos de la clase Varietal que representan los varietales del vino.
        """
        self.añada = añada
        self.fechaActualización = fechaActualizacion
        self.imagenEtiqueta = imagen
        self.nombre = nombre
        self.notaDeCataBodega = nota
        self.precioARS = precio
        self.bodega = bodega
        self.reseñas = reseñas
        self.varietales = varietales

    def tenesResenasDeTipoEnPeriodo(self, fechaDesde, fechaHasta):
        """
        Filtra las reseñas del vino que se encuentren en un período de tiempo y sean de tipo sommelier.

        Parámetros:
        - fechaDesde (str): Fecha de inicio del período.
        - fechaHasta (str): Fecha de fin del período.

        Retorna:
        - vinosQueCumplenConFiltros (list): Lista de objetos de la clase Reseña que cumplen con los filtros.
        """
        vinosQueCumplenConFiltros = []
        for i in range(len(self.reseñas)):
            enPeriodo = self.reseñas[i].sosDePeriodo(fechaDesde, fechaHasta)
            sosDeTipo = self.reseñas[i].sosDeSommelier()
            if enPeriodo and sosDeTipo:
                vinosQueCumplenConFiltros.append(self.reseñas[i])
        return vinosQueCumplenConFiltros

    def buscarInfoBodega(self):
        """
        Obtiene la información de la bodega del vino.

        Retorna:
        - nombreBodega (str): Nombre de la bodega.
        - region (str): Región de la bodega.
        - pais (str): País de la bodega.
        """
        nombreBodega = self.bodega.getNombre()
        region, pais = self.bodega.obtenerRegionYPais()
        return nombreBodega, region, pais

    def buscarVarietal(self):
        """
        Obtiene los varietales del vino.

        Retorna:
        - varietales (str): Descripción de los varietales del vino.
        """
        varietales = ""
        for i in self.varietales:
            varietales += str(i.getDescripcion())
        return varietales

    def calcularPuntajeDeSommelierEnPeriodo(self, fechaDesde, fechaHasta):
        """
        Calcula el puntaje promedio de las reseñas del vino que se encuentren en un período de tiempo y sean de tipo sommelier.

        Parámetros:
        - fechaDesde (str): Fecha de inicio del período.
        - fechaHasta (str): Fecha de fin del período.

        Retorna:
        - promPunt (float): Puntaje promedio de las reseñas que cumplen con los filtros.
        """
        puntajes = []
        for i in range(len(self.reseñas)):
            enPeriodo = self.reseñas[i].sosDePeriodo(fechaDesde, fechaHasta)
            esDeSommelier = self.reseñas[i].sosDeSommelier()
            if enPeriodo and esDeSommelier:
                puntajes.append(self.reseñas[i].getPuntaje())
        promPunt = self.calcularPuntajePromedio(puntajes)
        return promPunt

    def calcularPuntajePromedio(self, puntajes):
        """
        Calcula el puntaje promedio de una lista de puntajes.

        Parámetros:
        - puntajes (list): Lista de puntajes.

        Retorna:
        - promPuntajes (float): Puntaje promedio.
        """
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
    
