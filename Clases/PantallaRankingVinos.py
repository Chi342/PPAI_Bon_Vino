import tkinter as tk
from GestorRankingVinos import *
from tkcalendar import DateEntry


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

        self.solicitarSelFechaDesdeHasta()

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

        self.boton_validar_fecha = tk.Button(self.ventana_ranking, text='Validar', command=self.tomarSelFechas)
        self.boton_validar_fecha.grid(row=2, column=0, pady=15)

    def tomarSelFechaDesde(self):
        self.fechaDesde = self.calendario_desde.get_date()

    def tomarSelFechaHasta(self):
        self.fechaHasta = self.calendario_hasta.get_date()
    
    def tomarSelFechas(self):
        self.tomarSelFechaDesde()
        self.tomarSelFechaHasta()
        self.validarPeriodo()

    def validarPeriodo(self):
        print('ejecutar')
        if (self.fechaDesde != None and self.fechaHasta != None) and self.fechaDesde <= self.fechaHasta:
            print('borrando')
            self.calendario_desde.state(['disabled'])
            self.calendario_hasta.state(['disabled'])
            self.boton_validar_fecha.config(state='disabled')
            self.gestor.tomarSelFechaDesdeYHasta()
        else:
            self.ventana_emergente = tk.Toplevel(self.ventana_ranking)
            self.ventana_emergente.title('Error')
            self.ventana_emergente.geometry('360x360')

            self.etiqueta_emergente = tk.Label(self.ventana_emergente, text='Ingresar una fecha válida')
            self.etiqueta_emergente.grid(row=0, column=0)

            self.boton_emergente = tk.Button(self.ventana_emergente, text='Aceptar', command=self.ventana_emergente.destroy)
            self.boton_emergente.grid(row=1, column=0)

    def solicitarSelTipoReseña(self):

        self.opcion_filtro = tk.IntVar()
        
        self.filtro_normales = tk.Radiobutton(self.ventana_ranking, text='Reseñas normales', variable=self.opcion_filtro, value=1, indicatoron=0)
        self.filtro_sommelier = tk.Radiobutton(self.ventana_ranking, text='Reseñas de Sommelier', variable=self.opcion_filtro, value=2, indicatoron=0)
        self.filtro_amigos = tk.Radiobutton(self.ventana_ranking, text='Reseñas de Amigos', variable=self.opcion_filtro, value=3, indicatoron=0)

        self.filtro_normales.grid(row=4, column=0, padx=15, sticky='w')
        self.filtro_sommelier.grid(row=5, column=0, padx=15, pady=15, sticky='w')
        self.filtro_amigos.grid(row=6, column=0, padx=15, sticky='w')

        self.boton_reseña = tk.Button(self.ventana_ranking, text='Confirmar', command=self.tomarTipoReseña)
        self.boton_reseña.grid(row=7, column=0, pady=15)

    
    def tomarTipoReseña(self):
        resultado = 'Reseñas de Sommelier'
        self.filtro_normales.config(state='disabled')
        self.filtro_amigos.config(state='disabled')
        self.filtro_sommelier.config(state='disabled')
        self.boton_reseña.config(state='disabled')
        self.tipoReseña = resultado
        self.gestor.tomarSelTipoReseña()

    def solicitarSelTipoVisualizacion(self, ):
        self.opcion_visualizacion = tk.IntVar()
        
        self.pdf = tk.Radiobutton(self.ventana_ranking, text='Visualización PDF', variable=self.opcion_visualizacion, value=1, indicatoron=0)
        self.excel = tk.Radiobutton(self.ventana_ranking, text='Visualización en Excel', variable=self.opcion_visualizacion, value=2, indicatoron=0)
        self.pantalla = tk.Radiobutton(self.ventana_ranking, text='Visualización en pantalla', variable=self.opcion_visualizacion, value=3, indicatoron=0)

        self.pdf.grid(row=8, column=0, padx=15, sticky='w')
        self.excel.grid(row=9, column=0, padx=15, pady=15, sticky='w')
        self.pantalla.grid(row=10, column=0, padx=15, sticky='w')

        self.boton_visualizacion = tk.Button(self.ventana_ranking, text='Confirmar', command=self.tomarTipoVisualizacion)
        self.boton_visualizacion.grid(row=11, column=0, pady=15)

    def tomarTipoVisualizacion(self):
        resultado = 'Excel'
        self.pdf.config(state='disabled')
        self.excel.config(state='disabled')
        self.pantalla.config(state='disabled')
        self.boton_visualizacion.config(state='disabled')
        self.tipoVisualizacion = resultado
        self.gestor.tomarSelTipoVisualizacion()

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
        self.ventana_emergente.destroy()
        self.ventana_ranking.destroy()


    def tomarConfirmacionGenReporte(self):
        self.ventana_emergente.destroy()
        self.ventana_ranking.destroy()
        self.gestor.tomarConfirmacionGenReporte()

    def confirmarExportacion(self, ):
        pass