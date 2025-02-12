import psycopg2
from psycopg2 import sql

class PlayerDatabase():
    def __init__(self):
        # Hardcoded database credentials
        self.conn = psycopg2.connect(
            dbname="photon", 
            user="student", 
            password="student", 
            host="localhost"  
            #port = "5432"
        )

#still need to bounce back if there is no codename 
    def add_player(self, player_id, codename):
        with self.conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO players (id, codename) VALUES (%s, %s);
            ''', (player_id, codename))
        self.conn.commit()

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

    def close_connection(self):
        self.conn.close()




'''
(this is what I am testing w in main.py)


from PlayerDatabase import PlayerDatabase

class main:
    def __init__(self):
        self.db = PlayerDatabase()  # No need to pass credentials!

    def run(self):
        # Adding players
        self.db.add_player(500, 'BhodiLi')
        self.db.add_player(501, 'Alpha')

        # Retrieving player info
        print("Codename for ID 500:", self.db.get_codename_by_id(500))
        print("ID for codename 'Alpha':", self.db.get_id_by_codename('Alpha'))

        # Close DB connection
        self.db.close_connection()

# Run the application
if __name__ == "__main__":
    app = main()
    app.run()


'''

