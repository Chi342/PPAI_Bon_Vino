#!/usr/bin/python
#-*- coding: utf-8 -*-
import datetime

class Reseña:
    def __init__(self, comentario, esPremium, año, mes, dia, puntaje):
        """
        Inicializa una instancia de la clase Reseña.

        Parámetros:
        - comentario (str): El comentario de la reseña.
        - esPremium (bool): Indica si el usuario que realizó la reseña es premium.
        - año (int): El año de la fecha de la reseña.
        - mes (int): El mes de la fecha de la reseña.
        - dia (int): El día de la fecha de la reseña.
        - puntaje (int): El puntaje asignado a la reseña.
        """
        self.comentario = comentario
        self.esPremium = esPremium
        self.fechaReseña = datetime.datetime(año, mes, dia)
        self.puntaje = puntaje

    def sosDePeriodo(self, fechaDesde, fechaHasta):
        """
        Verifica si la reseña fue realizada dentro de un período de tiempo específico.

        Parámetros:
        - fechaDesde (datetime.date): La fecha de inicio del período.
        - fechaHasta (datetime.date): La fecha de fin del período.

        Retorna:
        - bool: True si la reseña fue realizada dentro del período, False en caso contrario.
        """
        fechaReseñaDate = self.fechaReseña.date()
        if fechaDesde < fechaReseñaDate < fechaHasta:
            return True
        return False
    
    def sosDeSommelier(self):
        """
        Verifica si el usuario que realizó la reseña es un sommelier premium.

        Retorna:
        - bool: True si el usuario es un sommelier premium, False en caso contrario.
        """
        return self.esPremium

    def getPuntaje(self):
        """
        Obtiene el puntaje asignado a la reseña.

        Retorna:
        - int: El puntaje asignado a la reseña.
        """
        return self.puntaje

