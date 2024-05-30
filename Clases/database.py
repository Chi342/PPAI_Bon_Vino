from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib

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