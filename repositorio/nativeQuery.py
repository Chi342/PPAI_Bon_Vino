from sqlalchemy import create_engine, text

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

# Obtiene una conexión
connection = engine.connect()

# Define la consulta SQL nativa
#sql_query = """SELECT id, añada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS    FROM vino"""
sql_query = text("""SELECT * FROM vino""")

# Ejecuta la consulta y obtén los resultados
result = connection.execute(sql_query)

# Itera sobre los resultados e imprime cada fila
for row in result:
    print("ID:", row[0])
    print("Año:", row[1])
    print("Fecha de actualización:", row[2])
    print("Imagen de etiqueta:", row[3])
    print("Nombre:", row[4])
    print("Nota de cata de bodega:", row[5])
    print("Precio en ARS:", row[6])
    print()

# Cierra la conexión
connection.close()
