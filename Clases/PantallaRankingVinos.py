import tkinter as tk
from tkcalendar import DateEntry
from GestorRankingVinos import *

class PantallaRankingVinos:
    def __init__(self, resolucion, nombre, icono, color, gestor):

        self.ventana_ranking = None
        self.gestor = gestor
        self.__resolucion = resolucion
        self.__nombre = nombre
        self.__icono = icono
        self.__color = color

        self.fechaDesde = None
        self.fechaHasta = None
        self.tipoReseña = None
        self.tipoVisualizacion = None
        self.confirmacion = None

    def opcGenerarRankingVinos(self):
        self.habilitarVentana()

    def habilitarVentana(self):
        self.ventana_ranking = tk.Tk()
        self.ventana_ranking.geometry(self.__resolucion)
        self.ventana_ranking.title(self.__nombre)
        self.ventana_ranking.iconbitmap(self.__icono)
        self.ventana_ranking.config(bg=self.__color)

        self.gestor.opcGenerarRankingVinos()
        self.boton_cancelar = tk.Button(self.ventana_ranking, text="Cancelar", command=self.gestor.finCU)

        self.boton_cancelar.place(x=250, y=600, anchor='s')
        self.ventana_ranking.mainloop()

    def solicitarSelFechaDesdeHasta(self):

        self.texto_desde = tk.Label(self.ventana_ranking, text='Fecha desde', padx=15)
        self.texto_hasta = tk.Label(self.ventana_ranking, text='Fecha hasta', padx=15)
        self.texto_desde.grid(row=0, column=0)
        self.texto_hasta.grid(row=1, column=0)

        self.calendario_desde = DateEntry(self.ventana_ranking, date_pattern='dd/mm/yyyy', date=None)
        self.calendario_hasta = DateEntry(self.ventana_ranking, date_pattern='dd/mm/yyyy', date=None)
        self.calendario_desde.grid(row=0, column=1, padx=15, pady=15)
        self.calendario_hasta.grid(row=1, column=1, padx=15)

        self.boton_validar_fecha = tk.Button(self.ventana_ranking, text='Validar', command=self.tomarSelFechaDesdeHasta)
        self.boton_validar_fecha.grid(row=2, column=0, pady=15)

    def tomarSelFechaDesdeHasta(self):
        self.fechaDesde = self.calendario_desde.get_date()
        self.fechaHasta = self.calendario_hasta.get_date()
        self.validarPeriodo()

    def validarPeriodo(self):
        if (self.fechaDesde != None and self.fechaHasta != None) and self.fechaDesde <= self.fechaHasta:
            self.calendario_desde.state(['disabled'])
            self.calendario_hasta.state(['disabled'])
            self.boton_validar_fecha.config(state='disabled')
            self.gestor.tomarSelFechaDesdeYHasta(self.fechaDesde, self.fechaHasta)
        else:
            self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
            self.ventana_emergente.title('Error')
            self.ventana_emergente.geometry('360x360')

            self.etiqueta_emergente = tk.Label(self.ventana_emergente, text='Ingresar una fecha válida')
            self.etiqueta_emergente.grid(row=0, column=0)

            self.boton_emergente = tk.Button(self.ventana_emergente, text='Aceptar', command=self.ventana_emergente.destroy)
            self.boton_emergente.grid(row=1, column=0)

    def solicitarSelTipoReseña(self):

        self.label_reseña = tk.Label(self.ventana_ranking, text='Elija el tipo de Reseña')

        self.filtro_normales = tk.Button(self.ventana_ranking, text="NORMAL", command=lambda: self.tomarTipoReseña("normal"))
        self.filtro_sommelier = tk.Button(self.ventana_ranking, text="SOMMELIER", command=lambda: self.tomarTipoReseña("sommelier"))
        self.filtro_amigos = tk.Button(self.ventana_ranking, text="AMIGO", command=lambda: self.tomarTipoReseña("amigo"))

        self.filtro_normales.grid(row=4, column=0, padx=15, sticky='w')
        self.filtro_sommelier.grid(row=5, column=0, padx=15, pady=15, sticky='w')
        self.filtro_amigos.grid(row=6, column=0, padx=15, sticky='w')

    def tomarTipoReseña(self, reseña):
        if(reseña == 'sommelier'):
            self.filtro_normales.config(state='disabled')
            self.filtro_amigos.config(state='disabled')
            self.filtro_sommelier.config(state='disabled')
            self.tipoReseña = reseña
            self.gestor.tomarSelTipoReseña(reseña)
        else:
            self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
            self.ventana_emergente.title('Error')
            self.ventana_emergente.geometry('360x360')

            self.etiqueta_emergente = tk.Label(self.ventana_emergente, text='Este CU trabaja con la opcion Sommelier')
            self.etiqueta_emergente.grid(row=0, column=0)

            self.boton_emergente = tk.Button(self.ventana_emergente, text='Aceptar', command=self.ventana_emergente.destroy)
            self.boton_emergente.grid(row=1, column=0)

    def solicitarSelTipoVisualizacion(self):
        self.label_visualizacion = tk.Label(self.ventana_ranking, text='Elija el tipo de visualizacion')
        self.pdf = tk.Button(self.ventana_ranking, text="PDF", command=lambda: self.tomarTipoVisualizacion("pdf"))
        self.excel = tk.Button(self.ventana_ranking, text="EXCEL", command=lambda: self.tomarTipoVisualizacion("excel"))
        self.pantalla = tk.Button(self.ventana_ranking, text="PANTALLA", command=lambda: self.tomarTipoVisualizacion("pantalla"))

        self.label_visualizacion.grid(row=11, column=0, padx=15, sticky='w')
        self.pdf.grid(row=12, column=0, padx=15, sticky='w')
        self.excel.grid(row=13, column=0, padx=15, pady=15, sticky='w')
        self.pantalla.grid(row=14, column=0, padx=15, sticky='w')

    def tomarTipoVisualizacion(self, visualizacion):
        if(visualizacion == 'excel'):
            self.pdf.config(state='disabled')
            self.excel.config(state='disabled')
            self.pantalla.config(state='disabled')
            self.tipoVisualizacion = visualizacion
            self.gestor.tomarSelTipoVisualizacion(visualizacion)
        else:
            self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
            self.ventana_emergente.title('Error')
            self.ventana_emergente.geometry('360x360')

            self.etiqueta_emergente = tk.Label(self.ventana_emergente, text='Este CU trabaja con la opcion Excel')
            self.etiqueta_emergente.grid(row=0, column=0)

            self.boton_emergente = tk.Button(self.ventana_emergente, text='Aceptar', command=self.ventana_emergente.destroy)
            self.boton_emergente.grid(row=1, column=0)

    def solicitarConfirmacionGenReporte(self):
        self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
        self.ventana_emergente.title('Confirmación del reporte')
        self.ventana_emergente.geometry('360x360')
        texto = 'Fecha desde: {} \n Fecha hasta: {} \n Tipo de reseña: {} \n Tipo de visualización: {}'.format(
            self.fechaDesde, self.fechaHasta, self.tipoReseña, self.tipoVisualizacion)
        self.etiqueta_emergente = tk.Label(self.ventana_emergente, text=texto)
        self.etiqueta_emergente.grid(row=0, column=0)

        self.boton_emergente = tk.Button(self.ventana_emergente, text='Cancelar', command=self.cancelarReporte)
        self.boton_emergente_confirmar = tk.Button(self.ventana_emergente, text='Confirmar', command=self.tomarConfirmacionGenReporte)
        self.boton_emergente.grid(row=1, column=0)
        self.boton_emergente_confirmar.grid(row=1, column=1)

    def cancelarReporte(self):
        if(self.tipoVisualizacion != None):
            self.ventana_emergente.destroy()
        self.ventana_ranking.destroy()

    def tomarConfirmacionGenReporte(self):
        self.ventana_emergente.destroy()
        self.gestor.tomarConfirmacionGenReporte()

    def confirmarExportacion(self, ):
        self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
        self.ventana_emergente.title('Reporte generado')
        self.ventana_emergente.geometry('360x360')

        self.etiqueta_emergente = tk.Label(self.ventana_emergente, text='Reporte generado con exito')
        self.etiqueta_emergente.grid(row=0, column=0)

        self.boton_emergente = tk.Button(self.ventana_emergente, text='Aceptar', command=self.gestor.finCU)
        self.boton_emergente.grid(row=1, column=0)
        
    def noHayReseñaSommelier(self):
        self.ventana_confirmacion = tk.Toplevel(self.ventana_ranking)
        self.ventana_confirmacion.title('No tiene reseñas de Sommelier')
        self.ventana_confirmacion.geometry('500x160')
        self.etiqueta_emergente = tk.Label(self.ventana_confirmacion, text='No se encontraron vinos con reseñas de sommelier en el periodo seleccionado')
        self.etiqueta_emergente.grid(row=0, column=0)

        self.boton_confirmacion = tk.Button(self.ventana_confirmacion, text='Aceptar', command=self.gestor.finCU)
        self.boton_confirmacion.grid(row=1, column=0)