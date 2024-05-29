import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib

from dominio.TodasLasClases import DTOVino

# Define the connection string
params = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=.;'
    'DATABASE=Bon_vino;'
    'Trusted_Connection=yes;'
)

# Create the SQLAlchemy engine
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
Session = sessionmaker(bind=engine)
session = Session()

# Display objects for each class
try:
    """Prints all the objects in the database.
    print("Bodegas:")
    bodegas = session.query(Bodega).all()
    for bodega in bodegas:
        print(bodega.__dict__)
        
    print("\nPaises:")
    paises = session.query(Pais).all()
    for pais in paises:
        print(pais.__dict__)

    print("\nProvincias:")
    provincias = session.query(Provincia).all()
    for provincia in provincias:
        print(provincia.__dict__)

    print("\nRegiones Vitivinícolas:")
    regiones = session.query(RegionVitivinicola).all()
    for region in regiones:
        print(region.__dict__)

    print("\nResenias:")
    resenias = session.query(Resenia).all()
    for resenia in resenias:
        print(resenia.__dict__)

    print("\nVarietales:")
    varietales = session.query(Varietal).all()
    for varietal in varietales:
        print(varietal.__dict__)

"""
    print("\nVinos:")
    vinos = session.query(DTOVino).all()
    for vino in vinos:
        print("ID:", vino.idVino)
        print("Añada:", vino.aniada)
        print("Fecha de actualización:", vino.fechaActualizacion)
        print("Imagen de etiqueta:", vino.imagenEtiqueta)
        print("Nombre:", vino.nombre)
        print("Nota de cata de bodega:", vino.notaDeCataBodega)
        print("Precio en ARS:", vino.precioARS)
#        print("Bodega:", vino.bodega)
        print()

except Exception as e:
    print(f"Error querying database: {e}")
finally:
    session.close()

# Configuración de la ventana principal de la aplicación
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('BonVino')
ventana.iconbitmap('dominio/extras/icono.ico')


def rankear_vinos():
    print('Ejecución del evento_click')
    calendario_desde.grid(row=1, column=1, pady=15)
    calendario_hasta.grid(row=2, column=1)
    boton_validar_fecha.grid(row=3, column=0, pady=15)

    texto_desde.grid(row=1, column=0)
    texto_hasta.grid(row=2, column=0)


def validar_fecha():
    fecha_desde = calendario_desde.get_date()
    fecha_hasta = calendario_hasta.get_date()
    if fecha_desde <= fecha_hasta:
        print('Correcto')
        tomar_filtro()
    else:
        print('Fecha incorrecta')


def tomar_filtro():
    opcion_filtro = tk.StringVar(value='')
    filtro_normales = tk.Radiobutton(ventana, text='Reseñas normales', variable=opcion_filtro, value='Reseñas normales', indicatoron=0)
    filtro_sommelier = tk.Radiobutton(ventana, text='Reseñas de Sommelier', variable=opcion_filtro, value='Reseñas de Sommelier', command=pedir_formato_reporte, indicatoron=0)
    filtro_amigos = tk.Radiobutton(ventana, text='Reseñas de Amigos', variable=opcion_filtro, value='Reseñas de amigos', indicatoron=0)

    for radio in (filtro_normales, filtro_sommelier, filtro_amigos):
        radio.config(background=ventana.cget('background'), borderwidth=1, relief='solid')

    filtro_normales.grid(row=4, column=0, sticky='w')
    filtro_sommelier.grid(row=5, column=0, sticky='w')
    filtro_amigos.grid(row=6, column=0, sticky='w')

    seleccion = opcion_filtro.get()
    print(seleccion)


def pedir_formato_reporte():
    texto_formato = tk.Label(ventana, text='Seleccionar formato de visualización')
    boton_pdf = ttk.Button(ventana, text='PDF')
    boton_excel = ttk.Button(ventana, text='Archivo Excel', command=mostrar_confirmacion)
    boton_pantalla = ttk.Button(ventana, text='Pantalla')

    texto_formato.grid(row=7, column=0, sticky='w')
    boton_pdf.grid(row=8, column=0, sticky='w', padx=15)
    boton_excel.grid(row=8, column=1, sticky='w', padx=15)
    boton_pantalla.grid(row=8, column=2, sticky='w', padx=15)


def mostrar_confirmacion():
    respuesta = messagebox.askyesno('Confirmacion', '¿Seguro?')
    if respuesta:
        print('confirmado')
        etiqueta_reporte_generado = ttk.Label(text='Reporte generado exitosamente...')
        etiqueta_reporte_generado.grid(row=9, column=0)
    else:
        print('Denegado')


# Creación de botones

boton1 = ttk.Button(ventana, text='Generar ranking vinos', command=rankear_vinos)
boton1.grid(row=0, column=0)

boton_validar_fecha = ttk.Button(ventana, text='Validar', command=validar_fecha)

calendario_desde = DateEntry(ventana, date_pattern='dd/mm/yyyy')
calendario_hasta = DateEntry(ventana, date_pattern='dd/mm/yyyy')

texto_desde = tk.Label(ventana, text='Fecha desde')
texto_hasta = tk.Label(ventana, text='Fecha hasta')



ventana.mainloop()