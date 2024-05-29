from PantallaRankingVinos import *
import tkinter as tk
from tkinter import PhotoImage, Menu
from GestorRankingVinos import *
from TodasLasClases import Vino
#from Vino import *
import random
import os
import datetime


def test():
    def generar_ranking_vinos():

        gestor = GestorRankingVinos(lista_vinos)
        pantalla_ranking = PantallaRankingVinos('360x720', 'BonVino - Generar ranking de vinos', 'Clases/extras/icono.ico', '#5C1D05', gestor)
        gestor.pantalla = pantalla_ranking
        pantalla_ranking.opcGenerarRankingVinos()


    def crear_menu():
        menu_principal = Menu(ventana)

        submenu_perfil = Menu(menu_principal, tearoff=0)
        submenu_perfil.add_command(label='Ver perfil')
        submenu_perfil.add_command(label='Salir')

        submenu_bodegas = Menu(menu_principal, tearoff=0)
        submenu_bodegas.add_command(label='Ver bodegas')

        submenu_actividades = Menu(menu_principal, tearoff=0)
        submenu_actividades.add_command(label='Generar ranking vinos', command=generar_ranking_vinos)
        submenu_actividades.add_command(label='Importar actualización de vinos de bodega')

        menu_principal.add_cascade(menu=submenu_perfil, label='Perfil')
        menu_principal.add_cascade(menu=submenu_bodegas, label='Bodegas')
        menu_principal.add_cascade(menu=submenu_actividades, label='Actividades')

        ventana.config(menu=menu_principal)


    def crear_lista_bodegas():
        bodegas = []
        for i in range(10):
            pass
        return bodegas


    def crear_lista_varietal():
        varietal = []
        for i in range(10):
            pass
        return varietal

    def cargar_vinos(lista_vinos):
        etiquetas = os.listdir('Clases/extras/etiquetas')
        nombres = ['Cabernet Sauvignon', 'Airén', 'Chardonnay', 'Syrah', 'Garnacha', 'Sauvignon Blanc', 'Trebbiano Toscano', 'Tempranillo']
        bodega = crear_lista_bodegas()
        varietal = crear_lista_varietal()
        for i in range(30):
            añada = random.randint(1990, 2023)
            año = random.randint(2000, 2023)
            mes = random.randint(1, 12)
            dia = random.randint(1, 28)
            fechaActualizacion = datetime.datetime(año, mes, dia)
            imagenEtiqueta = random.choice(etiquetas)
            nombre = random.choice(nombres)
            notaDeCataBodega = random.randint(1, 5)
            precioARS = random.randint(2000, 35000)

            nuevo_vino = Vino(añada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, varietal)
            lista_vinos.append(nuevo_vino)
        return lista_vinos


    lista_vinos = []
    lista_vinos = cargar_vinos(lista_vinos)

    ventana = tk.Tk()
    ventana.geometry('1280x720')
    ventana.title('BonVino')
    ventana.iconbitmap('Clases/extras/icono.ico')
    imagen_fondo = PhotoImage(file='Clases/extras/BonVINO.png')
    etiqueta_fondo = tk.Label(ventana, image=imagen_fondo)
    etiqueta_fondo.place(relwidth=1, relheight=1)


    crear_menu()
    ventana.mainloop()


if __name__ == '__main__':
    test()
