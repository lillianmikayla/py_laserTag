# databaseconnector.py
import psycopg2
from config import DB_CONFIG  # Import the configuration parameters

def connect_to_db():
    """
    Establishes a connection to the PostgreSQL database using the configuration
    defined in config.py.
    Returns the connection object and the cursor for executing queries.
    """
    try:
        # Connect to PostgreSQL using the parameters from config.py
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Return the connection and cursor for use in other parts of the app
        return conn, cursor

    except Exception as error:
        print(f"Error: {error}")
        return None, None  # Return None if connection fails