from PIL import Image, ImageTk
import tkinter as tk
import os
from tkinter import PhotoImage, Menu
from Clases.TodasLasClases import DTOVino
from Clases.PantallaRankingVinos import PantallaRankingVinos
from Clases.GestorRankingVinos import GestorRankingVinos
import sys
sys.path.append('/mnt/linux/repositories/PPAI_BON_VINO')

def main():
    """
    Función principal que crea una ventana de la aplicación BonVino y configura el menú.
    """
    def generar_ranking_vinos():
        """
        Muestra la pantalla.
        """
        gestor = GestorRankingVinos(lista_de_vinos)
        pantalla_ranking = PantallaRankingVinos('360x720', 'BonVino - Generar ranking de vinos', '/mnt/linux/repositories/PPAI_BON_VINO/Clases/extras/BonVINO.gif', '#5C1D05', gestor)
        gestor.pantalla = pantalla_ranking
        pantalla_ranking.opcGenerarRankingVinos()

    def crear_menu():
        """
        Crea el menú principal de la aplicación BonVino con sus respectivos submenús y opciones.
        """
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
        """
        Carga la lista de vinos desde una fuente de datos externa.
        
        Args:
            lista_vinos (list): La lista de vinos a cargar.
        
        Returns:
            list: La lista de vinos cargada.
        """
        vinos = DTOVino.consultar_vinos(lista_vinos)
        return lista_vinos
    
    lista_de_vinos = []
    lista_de_vinos = cargar_vinos(lista_de_vinos)

    ventana = tk.Tk()
    ventana.geometry('1280x720')
    ventana.title('BonVino')
    
    #ventana.iconbitmap('/mnt/linux/repositories/PPAI_BON_VINO/Clases/extras/icono.ico')
    image = Image.open('/mnt/linux/repositories/PPAI_BON_VINO/Clases/extras/BonVINO.gif')
    icono = ImageTk.PhotoImage(image)
    #ventana.wm_iconphoto(True, icono)
    ventana.iconphoto(True, icono)
    
    imagen_fondo = ImageTk.PhotoImage(file='/mnt/linux/repositories/PPAI_BON_VINO/Clases/extras/BonVINO.gif')
    etiqueta_fondo = tk.Label(ventana, image=imagen_fondo)
    etiqueta_fondo.place(relwidth=1, relheight=1)

    crear_menu()
    ventana.mainloop()

if __name__ == '__main__':
    main()