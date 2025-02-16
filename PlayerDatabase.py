import psycopg2
from psycopg2 import sql
import udpclient  

class PlayerDatabase():
    def __init__(self):
        # DB credentials
        self.conn = psycopg2.connect(
            dbname="photon", 
            user="student", 
            password="student", 
            host="localhost"
            #port="5432" still dk if we need this or not
        )

    def clear_database(self):
        """ Deletes all records from the players table 
            (probably should be called before each run)"""
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM players;")  
        self.conn.commit()
        print("Database cleared.")

    def add_player(self, player_id, codename):
        with self.conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO players (id, codename) VALUES (%s, %s);
            ''', (player_id, codename))
        self.conn.commit()
        udpclient.player_added()  # Call the function to add player

    def get_codename_by_id(self, player_id):
        with self.conn.cursor() as cursor:
            cursor.execute('''
                SELECT codename FROM players WHERE id = %s;
            ''', (player_id,))
            result = cursor.fetchone()
            return result[0] if result else None

    def get_id_by_codename(self, codename):
        with self.conn.cursor() as cursor:
            cursor.execute('''
                SELECT id FROM players WHERE codename = %s;
            ''', (codename,))
            result = cursor.fetchone()
            return result[0] if result else None

    def id_exists(self, player_id):
        """ Check if a player ID already exists and return the codename if it does """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT codename FROM players WHERE id = %s;", (player_id,))
            result = cursor.fetchone()
            return result[0] if result else None #returns None if ID isn't taken

    def print_database(self):
        """ Prints all records in the DB """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM players;")
            records = cursor.fetchall()
            if records:
                print("Database contents:")
                for record in records:
                    print(f"ID: {record[0]}, Codename: {record[1]}")
            else:
                print("Database is empty.")

    def close_connection(self):
        self.conn.close()
