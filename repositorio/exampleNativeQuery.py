from sqlalchemy import create_engine, text

from exampleLocalDatabaseConnection import DATABASE_URI

engine = create_engine(DATABASE_URI)

# Obtiene una conexión
connection = engine.connect()

# Define la consulta SQL nativa
#sql_query = """SELECT id, añada, fechaActualizacion, imagenEtiqueta, nombre, notaDeCataBodega, precioARS    FROM vino"""
sql_query = text("""SELECT * FROM Aeropuerto""")

# Ejecuta la consulta y obtén los resultados
result = connection.execute(sql_query)

# Imprime los resultados
for row in result:
    print(row)
    
# Cierra la conexión
connection.close()
