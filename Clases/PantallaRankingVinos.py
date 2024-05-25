#!/usr/bin/python
#-*- coding: utf-8 -*-

import tkinter as tk


class PantallaRankingVinos:
    def __init__(self, root):
        self.root = root
        self.root.title("Generar Ranking Vinos")

        self.label = tk.Label(self.root, text="Ingresa una fecha:")
        self.label.pack()
        self.fechaDesde = tk.Entry(self.root)
        self.fechaDesde.pack()
        
        self.fechaHasta = None
        self.tipoReseña = None
        self.tipoVisualizacion = None
        self.confirmacion = None

    def opcGenerarRankingVinos(self, ):
        pass

    def habilitarVentana(self, ):
        pass

    def solicitarSelFechaDesdeHasta(self, ):
        pass

    def tomarSelFechaDesde(self, ):
        pass

    def tomarSelFechaHasta(self, ):
        pass

    def validarPeriodo(self, ):
        pass

    def solicitarSelTipoReseña(self, ):
        pass

    def tomarTipoReseña(self, ):
        pass

    def solicitarSelTipoVisualizacion(self, ):
        pass

    def tomarTipoVisualizacion(self, ):
        pass

    def solicitarConfirmacionGenReporte(self, ):
        pass

    def tomarConfirmacionGenReporte(self, ):
        pass

    def confirmarExportacion(self, ):
        pass


root = tk.Tk()
app = PantallaRankingVinos(root)
root.mainloop()
