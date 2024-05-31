from PantallaRankingVinos import *
from tkinter import *
from Vino import *
from InterfazExcel import InterfazExcel


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
        if(self.tipoReseña == "sommelier"):
            self.pantalla.solicitarSelTipoVisualizacion()
        else:
            print('No se elijio la reseña sommelier')


    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion
        if(self.tipoVisualizacion == "excel"):
            self.pantalla.solicitarConfirmacionGenReporte()
        else:
            print('No se elijio la visualizacion Excel')

    def tomarConfirmacionGenReporte(self):
        self.buscarVinosConResenasEnPeriodo()

    def buscarVinosConResenasEnPeriodo(self):
        self.vinosQueCumplenConFiltros = []
        for vino in self.vinosOrdenados:
            if vino.tenesResenasDeTipoEnPeriodo(self.fechaDesde, self.fechaHasta):
                nombreDeVino = vino.nombre
                precioDeVino = vino.precioARS
                bodega, region, pais = vino.buscarInfoBodega()
                varietales = vino.buscarVarietal()
                listaVinos = [vino, nombreDeVino, precioDeVino, bodega, region, pais, varietales]
                self.vinosQueCumplenConFiltros.append(listaVinos)
        if len(self.vinosQueCumplenConFiltros) == 0:
            self.pantalla.noHayReseñaSommelier()
        else:
            self.calcularPuntajeDeSommelierEnPeriodo()

    def calcularPuntajeDeSommelierEnPeriodo(self, ):
        for vino in self.vinosQueCumplenConFiltros:
            vino.append(vino.calcularPuntajeDeSommelierEnPeriodo())
            
    def calcularPuntajeDeSommelierEnPeriodo(self):
        for vino in self.vinosQueCumplenConFiltros:
            puntaje = vino[0].calcularPuntajeDeSommelierEnPeriodo(self.fechaDesde, self.fechaHasta)
            vino.append(puntaje)
        self.ordenarVinos()
        
    def ordenarVinos(self, ):
        intExcel = InterfazExcel()
        self.vinosOrdenados = sorted(self.vinosQueCumplenConFiltros, key=lambda x: x[-1], reverse=True)
        intExcel.exportarExcel(self.vinosOrdenados)
        self.pantalla.confirmarExportacion()
        

    def finCU(self, ):
        self.pantalla.ventana_ranking.destroy()
        print('CU finalizado')
