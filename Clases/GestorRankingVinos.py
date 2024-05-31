from PantallaRankingVinos import *
from tkinter import *
from Vino import *
from InterfazExcel import InterfazExcel


class GestorRankingVinos:
    def __init__(self, lista_vinos):
        """
        Constructor de la clase GestorRankingVinos.

        Args:
        - lista_vinos: Lista de vinos a ser gestionados.
        """
        self.pantalla = None
        self.fechaDesde = None
        self.fechaHasta = None
        self.tipoReseña = None
        self.tipoVisualizacion = None
        self.vinosOrdenados = lista_vinos
        self.vinosQueCumplenConFiltros = None

    def opcGenerarRankingVinos(self):
        """
        Método que se encarga de solicitar al usuario las fechas de inicio y fin del período para generar el ranking de vinos.
        """
        self.pantalla.solicitarSelFechaDesdeHasta()

    def tomarSelFechaDesdeYHasta(self, fecha_desde, fecha_hasta):
        """
        Método que toma las fechas seleccionadas por el usuario y las guarda en las variables correspondientes.

        Args:
        - fecha_desde: Fecha de inicio del período seleccionado.
        - fecha_hasta: Fecha de fin del período seleccionado.
        """
        self.fechaDesde = fecha_desde
        self.fechaHasta = fecha_hasta
        self.pantalla.solicitarSelTipoReseña()

    def validarPeriodo(self, fecha_desde, fecha_hasta, validado):
        """
        Método que valida si el período seleccionado es válido, es decir, si la fecha de inicio es menor o igual a la fecha de fin.

        Args:
        - fecha_desde: Fecha de inicio del período seleccionado.
        - fecha_hasta: Fecha de fin del período seleccionado.
        - validado: Variable booleana que indica si el período es válido o no.

        Returns:
        - validado: Valor booleano que indica si el período es válido o no.
        """
        if fecha_desde <= fecha_hasta:
            validado = True
        else:
            validado = False
        return validado

    def tomarSelTipoReseña(self, tipoReseña):
        """
        Método que toma el tipo de reseña seleccionado por el usuario y realiza acciones dependiendo del tipo.

        Args:
        - tipoReseña: Tipo de reseña seleccionado por el usuario.
        """
        self.tipoReseña = tipoReseña
        if(self.tipoReseña == "sommelier"):
            self.pantalla.solicitarSelTipoVisualizacion()
        else:
            print('No se eligió la reseña sommelier')

    def tomarSelTipoVisualizacion(self, tipoVisualizacion):
        """
        Método que toma el tipo de visualización seleccionado por el usuario y realiza acciones dependiendo del tipo.

        Args:
        - tipoVisualizacion: Tipo de visualización seleccionado por el usuario.
        """
        self.tipoVisualizacion = tipoVisualizacion
        if(self.tipoVisualizacion == "excel"):
            self.pantalla.solicitarConfirmacionGenReporte()
        else:
            print('No se eligió la visualización Excel')

    def tomarConfirmacionGenReporte(self):
        """
        Método que se encarga de buscar los vinos que cumplen con los filtros seleccionados por el usuario.
        """
        self.buscarVinosConResenasEnPeriodo()

    def buscarVinosConResenasEnPeriodo(self):
        """
        Método que busca los vinos que tienen reseñas en el período seleccionado por el usuario.
        """
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

    def calcularPuntajeDeSommelierEnPeriodo(self):
        """
        Método que calcula el puntaje de sommelier para cada vino que cumple con los filtros seleccionados.
        """
        for vino in self.vinosQueCumplenConFiltros:
            vino.append(vino.calcularPuntajeDeSommelierEnPeriodo())

    def calcularPuntajeDeSommelierEnPeriodo(self):
        """
        Método que calcula el puntaje de sommelier para cada vino que cumple con los filtros seleccionados.
        """
        for vino in self.vinosQueCumplenConFiltros:
            puntaje = vino[0].calcularPuntajeDeSommelierEnPeriodo(self.fechaDesde, self.fechaHasta)
            vino.append(puntaje)
        self.ordenarVinos()
    def ordenarVinos(self):
        """
        Método que ordena los vinos según su puntaje de sommelier y exporta los resultados a un archivo Excel.
        """
        intExcel = InterfazExcel()
        self.vinosOrdenados = sorted(self.vinosQueCumplenConFiltros, key=lambda x: x[-1], reverse=True)
        intExcel.exportarExcel(self.vinosOrdenados)
        self.pantalla.confirmarExportacion()
        

    def finCU(self):
        """
        Método que se ejecuta al finalizar el caso de uso y cierra la ventana de ranking.
        """
        self.pantalla.ventana_ranking.destroy()
