#(this is what I am testing w in main.py)

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



