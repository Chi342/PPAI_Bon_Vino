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

