from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Define the connection string
connection_string = os.environ.get("DB_CONNECTION_STRING")

if connection_string is not None:
    print(f"DB_CONNECTION_STRING: {connection_string}")
else:
    print("DB_CONNECTION_STRING environment variable is not set")

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

# Check the connection
try:
    engine.connect()
    print("Connection successful!")

    # Fetch the first record from the "bodega" table
    with engine.connect() as connection:
        result = connection.execute(text("SELECT TOP 1 * FROM Bodega"))
        record = result.fetchone()
        print("First record from 'bodega' table:", record)

except Exception as e:
    print("Connection failed:", str(e))