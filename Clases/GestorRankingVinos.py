from PantallaRankingVinos import *
from tkinter import *

from Clases.Vino import *


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


    def tomarSelFechaDesdeYHasta(self):
        self.fechaDesde = self.pantalla.fechaDesde
        self.fechaHasta = self.pantalla.fechaHasta
        print('Las fechas:', self.fechaDesde, self.fechaHasta)

        self.pantalla.solicitarSelTipoReseña()

        
    def validarPeriodo(self, fecha_desde, fecha_hasta, validado):
        if fecha_desde <= fecha_hasta:
            validado = True
        else:
            validado = False
        return validado

    def tomarSelTipoReseña(self, tipoReseña):
        self.tipoReseña = tipoReseña
        print(self.tipoReseña)
        
        self.pantalla.solicitarSelTipoVisualizacion()


    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion
        print(self.tipoVisualizacion)
        self.pantalla.solicitarConfirmacionGenReporte()

    def tomarConfirmacionGenReporte(self):
        self.buscarVinosConResenasEnPeriodo()

    def buscarVinosConResenasEnPeriodo(self):
        self.vinosQueCumplenConFiltros = []
        for vino in self.vinosOrdenados:
            if vino.tenesResenasDeTipoEnPeriodo(self.fechaDesde, self.fechaHasta):
                self.vinosQueCumplenConFiltros.append(vino)
        for vino in self.vinosQueCumplenConFiltros:
            print(vino)
            for resena in vino.resenas:
                print(resena)
            
    def calcularPuntajeDeSommelierEnPeriodo(self, ):
        pass

    def ordenarVinos(self, ):
        pass

    def finCU(self, ):
        pass
