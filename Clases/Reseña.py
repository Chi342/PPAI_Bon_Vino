#!/usr/bin/python
#-*- coding: utf-8 -*-
import datetime


class Reseña:
    def __init__(self, comentario, esPremium, año, mes, dia, puntaje):
        self.comentario = comentario
        self.esPremium = esPremium
        self.fechaReseña = datetime.datetime(año, mes, dia)
        self.puntaje = puntaje

    def sosDePeriodo(self, fechaDesde, fechaHasta):
        fechaReseñaDate = self.fechaReseña.date()
        if fechaDesde < fechaReseñaDate < fechaHasta:
            return True
        return False
    
    def sosDeSommelier(self, ):
        return self.esPremium

    def getPuntaje(self, ):
        return self.puntaje

    # def getComentario(self, ):
    #     pass

    # def setComentario(self, value):
    #     pass

    # def setEsPremium(self, value):
    #     pass

    # def getFechaReseña(self, ):
    #     pass

    # def setFechaReseña(self, value):
    #     pass

    # def setPuntaje(self, value):
    #     pass


fecha1 = datetime.datetime(2022, 5, 12)
fecha2 = datetime.datetime(2021, 5, 12)
print(fecha1 > fecha2)
