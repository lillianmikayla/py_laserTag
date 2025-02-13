
'''
Code I used in the main file for testing:



from PlayerDatabase import PlayerDatabase

class main:
    def __init__(self):
        self.db = PlayerDatabase()  

    def run(self):

        # Clear database first
        self.db.clear_database()

        # Add the first player (will work)
        if not self.db.id_exists(500):
            print("ID 500 not found, adding BhodiLi...")
            self.db.add_player(500, 'BhodiLi')
        else:
            print("ID is taken by", self.db.id_exists(500))

        # Add second player (will work)
        if not self.db.id_exists(501):
            print("ID 501 not found, adding Alpha...")
            self.db.add_player(501, 'Alpha')
        else:
            print("ID is taken by", self.db.id_exists(501))

        # Add third player (will not work bc duplicate ID)
        if not self.db.id_exists(501):
            print("ID 501 not found, adding Shadynasty...")
            self.db.add_player(501, 'Shadynasty')
        else:
            print("ID is taken by", self.db.id_exists(501))

        print("ID for codename 'BhodiLi':", self.db.get_id_by_codename('BhodiLi'))
        print("Codename for ID 501:", self.db.get_codename_by_id(501))
        print("ID for codename 'Shadynasty':", self.db.get_id_by_codename('Shadynasty')) #should return none

        # Print entire database
        self.db.print_database()

        self.db.close_connection()

# Run the application
if __name__ == "__main__":
    app = main()
    app.run()



EXPECTED OUTPUT:

Database cleared.
ID 500 not found, adding BhodiLi...
ID 501 not found, adding Alpha...
ID is taken by Alpha
ID for codename 'BhodiLi' : 500
Codename for ID 501: Alpha
ID for codename 'Shadynasty' : None
Database contents:
ID 500, Codename: BhodiLi
ID 501, Codename: Alpha


'''
