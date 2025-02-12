# main.py
from databaseconnector import connect_to_db  # Import the database connector function

def main():
    print("Laser Tag")
    # Connect to the database using the function from databaseconnector.py
    conn, cursor = connect_to_db()

    if conn and cursor:
        print("Successfully connected to the database!")

        # Example: Fetch all players from the database
        cursor.execute("SELECT * FROM players;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Example: Insert a new player (you can modify this part as needed)
        cursor.execute('''
            INSERT INTO players (id, codename) 
            VALUES (%s, %s);
        ''', ('501', 'PlayerOne'))  # Insert a player with ID and codename
        conn.commit()  # Commit the transaction

        # Close the cursor and connection
        cursor.close()
        conn.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()