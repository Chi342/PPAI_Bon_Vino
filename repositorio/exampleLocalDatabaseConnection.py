from sqlalchemy import create_engine, text

# Configura la conexión a la base de datos
# Connection setup using Windows Authentication
DATABASE_URI = (
    'mssql+pyodbc:///?odbc_connect='
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MAIN;'
    'DATABASE=DBM;'
    'Trusted_Connection=yes;'
)
engine = create_engine(DATABASE_URI)