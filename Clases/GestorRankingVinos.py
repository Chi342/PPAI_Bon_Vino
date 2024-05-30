from PantallaRankingVinos import *
from tkinter import *


class GestorRankingVinos:
    def __init__(self, lista_vinos):

        self.pantalla = None
        self.fechaDesde = None
        self.fechaHasta = None
        self.tipoReseña = None
        self.tipoVisualizacion = None
        self.vinosOrdenados = lista_vinos
        self.vinosQueCumplenConFiltros = None

    def opcGenerarRankingVinos(self):
        self.pantalla.solicitarSelFechaDesdeHasta()


    def tomarSelFechaDesdeYHasta(self, fecha_desde, fecha_hasta):
        self.fechaDesde = fecha_desde
        self.fechaHasta = fecha_hasta
        self.pantalla.solicitarSelTipoReseña()

    def validarPeriodo(self, fecha_desde, fecha_hasta, validado):
        if fecha_desde <= fecha_hasta:
            validado = True
        else:
            validado = False
        return validado

    def tomarSelTipoReseña(self, reseña):
        self.tipoReseña = reseña
        if(self.tipoReseña == "sommelier"):
            self.pantalla.solicitarSelTipoVisualizacion()
        else:
            print('No se elijio la reseña sommelier')


    def tomarSelTipoVisualizacion(self, visualizacion):
        self.tipoVisualizacion = visualizacion
        if(self.tipoVisualizacion == "excel"):
            self.pantalla.solicitarConfirmacionGenReporte()
        else:
            print('No se elijio la visualizacion Excel')

    def tomarConfirmacionGenReporte(self):
        self.buscarVinosConResenasEnPeriodo()

    def buscarVinosConResenasEnPeriodo(self, ):
        pass

    def calcularPuntajeDeSommelierEnPeriodo(self, ):
        pass

    def ordenarVinos(self, ):
        pass

    def finCU(self, ):
        pass
