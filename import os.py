from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

# Get the value of the environment variable
db_password_aircon = os.getenv('DB_PASSWORD_AIRCON')

# Print the value
print(f"DB_PASSWORD_AIRCON: {db_password_aircon}")