import psycopg2
from psycopg2 import sql

class PlayerDatabase():
    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    # Method to add a new player
    def add_player(conn, player_id, codename):
        with conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO players (id, codename) VALUES (%s, %s);
            ''', (player_id, codename))
        conn.commit()  # Save changes

    # Method to get codename by player ID
    def get_codename_by_id(conn, player_id):
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT codename FROM players WHERE id = %s;
            ''', (player_id,))
            result = cursor.fetchone()
            return result[0] if result else None  # Return codename or None if not found

    # Method to get player ID by codename
    def get_id_by_codename(conn, codename):
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT id FROM players WHERE codename = %s;
            ''', (codename,))
            result = cursor.fetchone()
            return result[0] if result else None  # Return ID or None if not found

    def close_connection(self):
        self.conn.close()  # Close database connection