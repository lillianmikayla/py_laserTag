from PlayerDatabase import PlayerDatabase


class main:
    
    def __init__(self):
        # Update credentials here
        self.db = PlayerDatabase(
            dbname="photon", 
            user="student", 
            password="student", 
            host="localhost"
            #'port': 5432
        )

    def run(self):
        self.db.add_player(500, 'BhodiLi')
        print("Codename for ID 500:", self.db.get_codename_by_id(500))
        self.db.close_connection()

if __name__ == "__main__":
    app = main()
    app.run()