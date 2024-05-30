import sys
sys.path.append('C:/Users/Roberto/source/repos/robertoutn/PPAI_BON_VINO/')
import tkinter as tk
from tkinter import PhotoImage, Menu
import sys

import GestorRankingVinos
import PantallaRankingVinos
import tkinter as tk
from tkinter import PhotoImage, Menu
import sys
import GestorRankingVinos
import PantallaRankingVinos
from dominio.TodasLasClases import *
from Clases.Vino import *

def test():
    def generar_ranking_vinos():

        gestor = GestorRankingVinos(lista_de_vinos)
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


    def cargar_vinos(lista_vinos):
        vinos = DTOVino.consultar_vinos(lista_vinos)  # Assuming there is a static method 'consultar_vinos' in the 'Vino' class
    #    lista_vinos.extend(vinos)
        return lista_vinos


    # Crear una lista vacía de vinos
    lista_de_vinos = []
    
    # Llamar a la función cargar_vinos con la lista de vinos como argumento
    lista_de_vinos = cargar_vinos(lista_de_vinos)
    
    # Ahora, lista_de_vinos debería contener los vinos cargados por la función
    print("\nVinos:")
    for vino in lista_de_vinos:
        print("Añada:", vino.añada)
        print("Fecha de actualización:", vino.fechaActualización)
        print("Imagen de etiqueta:", vino.imagenEtiqueta)
        print("Nombre:", vino.nombre)
        print("Nota de cata de bodega:", vino.notaDeCataBodega)
        print("Precio en ARS:", vino.precioARS)
        print("Bodega:", vino.bodega)
        for resenia in vino.reseñas:
            print("Reseña:", resenia)
        
    print("\nCantidad de vinos cargados:", len(lista_de_vinos))
    
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
