from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Define the connection string
server = os.getenv("DB_SERVER_NAME_AIRCON")
username = os.getenv("DB_USERNAME_AIRCON")
password = os.getenv("DB_PASSWORD_AIRCON")


if not password or not username or not server:
    raise ValueError("Missing required environment variables")

    # Print the value
    print(f"DB_USERNAME_AIRCON:{username}, DB_PASSWORD_AIRCON: {password}, DB_SERVER_NAME_AIRCON: {server}")

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