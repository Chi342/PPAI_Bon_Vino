from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mapeo import Vino  # Asegúrate de importar tu clase Vino desde el archivo donde está definida

# Configura la conexión a la base de datos
# Connection setup using Windows Authentication
DATABASE_URI = (
    'mssql+pyodbc:///?odbc_connect='
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAIN;'
    'DATABASE=Bon_vino;'
    'Trusted_Connection=yes;'
)
engine = create_engine(DATABASE_URI)

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Obtiene todos los objetos mapeados de la tabla Vino
vinos = session.query(Vino).all()

# Itera sobre los objetos mapeados y muestra sus atributos
for vino in vinos:
    print("ID:", vino.id)
    print("Añada:", vino.añada)
    print("Fecha de actualización:", vino.fechaActualizacion)
    print("Imagen de etiqueta:", vino.imagenEtiqueta)
    print("Nombre:", vino.nombre)
    print("Nota de cata de bodega:", vino.notaDeCataBodega)
    print("Precio en ARS:", vino.precioARS)
    print()
