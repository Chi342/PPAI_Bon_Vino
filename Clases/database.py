from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
import os

# Define the connection string
username = os.environ.get("DB_USERNAME_AIRCON")
password = os.environ.get("DB_PASSWORD_AIRCON")
server = os.environ.get("DB_SERVER_NAME_AIRCON")
database = "Bon_vino"
driver = "ODBC+Driver+17+for+SQL+Server"

# Check if the required environment variables are set
if not username or not password or not server:
    raise ValueError("Missing required environment variables")

# Continue with the rest of the code
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

""" # Check the connection
try:
    engine.connect()
    print("Connection successful!")

    # Fetch the first record from the "bodega" table
    with engine.connect() as connection:
        result = connection.execute(text("SELECT TOP 1 * FROM Bodega"))
        record = result.fetchone()
        print("First record from 'bodega' table:", record)

except Exception as e:
    print("Connection failed:", str(e)) """