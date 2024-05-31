import tkinter as tk
import sys
#sys.path.append('C:/Users/Roberto/source/repos/robertoutn/PPAI_BON_VINO/')
import urllib

from sqlalchemy.orm import sessionmaker

from TodasLasClases import *
from tkinter import PhotoImage, Menu
from PantallaRankingVinos import PantallaRankingVinos
from GestorRankingVinos import GestorRankingVinos
from Vino import *
from TodasLasClases import DTOVino, DTOVarietal

def test():
    def generar_ranking_vinos():

        gestor = GestorRankingVinos(lista_de_vinos)
        pantalla_ranking = PantallaRankingVinos('360x720', 'BonVino - Generar ranking de vinos', 'extras/icono.ico', '#5C1D05', gestor)
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

    def crear_lista_resenias(i, vinos):
            # Add your implementation here
            resenias = session.query(DTOResenia).filter(DTOResenia.idVino == vinos[i].idVino).all()
            resenia = []
            for r in resenias:
                idResenia = r.id
                comentario = r.comentario
                premium = r.premium
                fechaResenia = r.fechaResenia
                puntaje = r.puntaje
                idVino = r.idVino
                resenia.append(Reseña(comentario, premium, fechaResenia.year, fechaResenia.month, fechaResenia.day, puntaje))
            return resenia

    def crear_lista_varietales(i, vinos):
        # Add your implementation here
        varietales = session.query(DTOVarietal).filter(DTOVarietal.idVino == vinos[i].idVino).all()
        lista_varietales = []
        for v in varietales:
            descripcion = v.descripcion
            porcentajeComposicion = v.porcentajeComposicion
            lista_varietales.append(Varietal(descripcion, porcentajeComposicion))
        return lista_varietales

    def cargar_vinos(vinos):
        etiquetas = os.listdir('extras/etiquetas')
        for i in range(len(vinos)):
            idVino = i
            añada = vinos[i].aniada
            fechaActualizacion = vinos[i].fechaActualizacion
            imagenEtiqueta = random.choice(etiquetas)
            nombre = vinos[i].nombre
            notaDeCataBodega=vinos[i].notaDeCataBodega
            precioARS = vinos[i].precioARS
            resenias = crear_lista_resenias(i, vinos)
            varietales = crear_lista_varietales(i, vinos)

            bodega = session.query(DTOBodega).filter(DTOBodega.id == vinos[i].bodega).first()

            regionVitivinicola = session.query(DTORegionVitivinicola).filter(DTORegionVitivinicola.id == bodega.regionVitivinicola).first()

            provincia = session.query(DTOProvincia).filter(DTOProvincia.id == regionVitivinicola.provincia).first()
            pais = session.query(DTOPais).filter(DTOPais.id == provincia.pais).first()
            pais = Pais(pais.nombre)
            provincia = Provincia(provincia.nombre, pais)
            regionVitivinicola = RegionVitivinicola(regionVitivinicola.nombre, regionVitivinicola.descripcion, provincia)

            bodega = Bodega(bodega.coordenadasUbicacion, bodega.descripcion, bodega.historia, bodega.nombre, bodega.periodoActualizacion, regionVitivinicola)
            nuevo_vino = Vino(añada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, resenias, varietales)
            lista_vinos.append(nuevo_vino)
        return lista_vinos

    # Crear una lista vacía de vinos
    lista_vinos = []

    engine = create_engine(f'mssql+pyodbc:///?odbc_connect=' 
                           'DRIVER={ODBC Driver 17 for SQL Server};'
                           'SERVER=DESKTOP-BFMGAUT\SQLEXPRESS;'
                           'DATABASE=Bon_vino;'
                           'Trusted_Connection=yes;')
    Session = sessionmaker(bind=engine)
    session = Session()
    # Llamar a la función cargar_vinos con la lista de vinos como argumento
    lista_de_vinos = cargar_vinos(lista_vinos)
    
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
    ventana.iconbitmap('extras/icono.ico')
    imagen_fondo = PhotoImage(file='extras/BonVINO.png')
    etiqueta_fondo = tk.Label(ventana, image=imagen_fondo)
    etiqueta_fondo.place(relwidth=1, relheight=1)

    crear_menu()
    ventana.mainloop()


if __name__ == '__main__':
    test()
