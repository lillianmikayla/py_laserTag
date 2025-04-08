import dearpygui.dearpygui as dpg
import time
import udpclient
import threading
import multiprocessing
#from udpserver import start_udp_server

from PIL import Image, ImageTk
import tkinter as tk
import time

from PlayerDatabase import PlayerDatabase

#git pull origin

#player DB class, previously class main in the database main.py test file
#commented out when not testing in VM

class PlayerDBApp:
    def __init__(self):
        self.db = PlayerDatabase()  # No need to pass credentials!
        self.localPlayerCount = 0

    def flush(self):
        self.db.clear_database()
        self.db.add_player(500, 'BhodiLi')
        self.db.add_player(501, 'Alpha')
        
    def runTest(self):
        # Adding players
        self.db.add_player(500, 'BhodiLi')
        self.db.add_player(501, 'Alpha')

        # Retrieving player info
        print("Codename for ID 500:", self.db.get_codename_by_id(500))
        print("ID for codename 'Alpha':", self.db.get_id_by_codename('Alpha'))

        # Close DB connection
        #self.db.close_connection()
        
    def checkID(self, id):
        #check for ID
        IDcheck = self.db.id_exists(id)
        if IDcheck == None:
            #add ID, prompt for codename
            return None
        else:
            self.localPlayerCount += 1
            #udpclient.player_added(self.localPlayerCount)
            return IDcheck
    
    def addPlayer(self, id, codename):
        #add player to database
        self.db.add_player(id, codename)
        self.localPlayerCount += 1
        #udpclient.player_added(self.localPlayerCount)
        
# class fakeDatabase:
#     def __init__(self):
#         self.localPlayerCount = 0
#         self.fakeDatabase = {}

#     def flush(self):
#         self.fakeDatabase.clear()
#         self.fakeDatabase[500] = 'BhodiLi'
#         self.fakeDatabase[501] = 'Alpha'
        
#     def runTest(self):
#         # Adding players
#         self.fakeDatabase[500] = 'BhodiLi'
#         self.fakeDatabase[501] = 'Alpha'

#         # Retrieving player info
#         print("Codename for ID 500:", self.fakeDatabase[500])

#         # Close DB connection
#         #self.db.close_connection()
        
#     def checkID(self, id):
#         #check for ID
#         IDcheck = self.fakeDatabase.get(id)
#         if IDcheck is None:
#             #add ID, prompt for codename
#             return None
#         else:
#             self.localPlayerCount += 1
#             #udpclient.player_added(self.localPlayerCount)
#             return IDcheck
    
#     def addPlayer(self, id, codename):
#         #add player to database
#         self.fakeDatabase[id] = codename
#         self.localPlayerCount += 1
#         #udpclient.player_added(self.localPlayerCount)

#callback section: sender = table cell ID, app_data = value in cell, user_data = tuple of (row, column, app)

#dictionary to store player codenames, used to display on play action screen
player_codenames = {
    "red": {},
    "green": {}
}

player_scores= {
    "red": {},
    "green": {}
}


#listening to hits on client port (7501)
def listen_for_hits():
    bufferSize = 1024
    localIP = "127.0.0.1"
    localPort = 7501  #client port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((localIP, localPort))

    print(f"Listening for hit messages on {localIP}:{localPort}")

    while True:
        data, addr = server_socket.recvfrom(bufferSize)
        message = data.decode('utf-8')
        print(f"Received game hit: {message}")

        # you can send a response after the above code
        # like stop game

def input_id_callback(sender, app_data, user_data):
    #invalid theme for handling invalid input scenario
    with dpg.theme() as invalid_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background when hovered
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background when active
    
    if app_data <= 0:
        dpg.bind_item_theme(sender, invalid_theme) 
        dpg.set_value(sender, 0) 
        return
    else:
        appAcc = user_data[2]
        check = appAcc.checkID(app_data)
        #case where ID is not in database
        if check == None:
            if (sender == f"redTable_{user_data[0]}"):
                dpg.configure_item(f"redTable_codename_{user_data[0]}", readonly=False, hint="Enter Codename")
                dpg.configure_item(f"redTable_equipment_{user_data[0]}", readonly=False)
                dpg.bind_item_theme(sender, 0)
            elif (sender == f"greenTable_{user_data[0]}"):
                dpg.configure_item(f"greenTable_codename_{user_data[0]}", readonly=False, hint="Enter Codename")
                dpg.configure_item(f"greenTable_equipment_{user_data[0]}", readonly=False)
                dpg.bind_item_theme(sender, 0)
            return
        #ID is in database
        else:
            if sender == f"redTable_{user_data[0]}":
                # Set the codename to the value stored in check
                dpg.set_value(f"redTable_codename_{user_data[0]}", check)
                player_codenames["red"][user_data[0]] = check # store red codename in dictionary
                player_scores["red"][user_data[0]] = 0  # store red score in dictionary
                dpg.configure_item(f"redTable_equipment_{user_data[0]}", readonly=False)
                dpg.bind_item_theme(sender, 0)
            elif sender == f"greenTable_{user_data[0]}":
                dpg.set_value(f"greenTable_codename_{user_data[0]}", check)
                player_codenames["green"][user_data[0]] = check
                player_scores["green"][user_data[0]] = 0
                dpg.configure_item(f"greenTable_equipment_{user_data[0]}", readonly=False) 
                dpg.bind_item_theme(sender, 0)
            return
        
def input_codename_callback(sender, app_data, user_data):
    idValue = None
    if "redTable" in sender:
        idValue = dpg.get_value(f"redTable_{user_data[0]}")
        player_codenames["red"][user_data[0]] = app_data # store red codename in dictionary
        player_scores["red"][user_data[0]] = 0  # store red score in dictionary
    elif "greenTable" in sender:
        idValue = dpg.get_value(f"greenTable_{user_data[0]}")
        player_codenames["green"][user_data[0]] = app_data 
        player_scores["green"][user_data[0]] = 0
    appAcc = user_data[2]
    appAcc.addPlayer(idValue, app_data)
    
def input_equipID_callback(sender, app_data, user_data): 
    equipment_id_str = str(app_data)
    udpclient.inputEquipID(equipment_id_str)

def network_swap_callback(sender, app_data, user_data):
    #further modification to handle bad IP needed (?)
    udpclient.change_network(app_data)
    #print("Previously Linked to server")

def show_main_window(app):
    dpg.delete_item("Splash Window")
       
    #Red team entry table    
    with dpg.window(tag="RedTable", pos=(0, 0), width=450, height=410,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as redTeam:
        dpg.add_text("Red Team", parent=redTeam)
        with dpg.table(header_row=True, label = "Red Team") as table_red_id:
            dpg.add_table_column(label = "Player Number", width_fixed=True,width=100)
            dpg.add_table_column(label = "Player ID", width_fixed=True,width=80)
            dpg.add_table_column(label = "Player Codename", width_fixed=True,width=180)
            dpg.add_table_column(label = "Equip. ID", width_fixed=True,width=80)

            for i in range(15):
                with dpg.table_row(parent=table_red_id) as row_red_id:
                    for j in range(4):
                        if j == 0:
                            dpg.add_text(f"Player {i + 1}")
                        elif j == 1:
                            dpg.add_input_int(callback=input_id_callback, user_data=(i, j, app), on_enter=True, parent=row_red_id, step=0, step_fast=0, width = 80, tag=f"redTable_{i}")
                        elif j == 2:
                            dpg.add_input_text(callback=input_codename_callback, user_data=(i, j, app), on_enter=True, parent=row_red_id, hint="Awaiting ID", width = 150, readonly=True, tag=f"redTable_codename_{i}")
                        elif j == 3:
                            dpg.add_input_int(callback=input_equipID_callback, user_data=(i, j, app), on_enter=True, parent=row_red_id, step=0, step_fast=0, readonly=True, width = 80, tag=f"redTable_equipment_{i}")

    #Green team entry table
    with dpg.window(tag="GreenTable", pos=(450, 0), width=450, height=410,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as greenTeam:
        dpg.add_text("Green Team", parent=greenTeam)
        with dpg.table(header_row=True, label = "Green Team") as table_green_id:
            dpg.add_table_column(label = "Player Number", width_fixed=True,width=100)
            dpg.add_table_column(label = "Player ID", width_fixed=True,width=80)
            dpg.add_table_column(label = "Player Codename", width_fixed=True,width=180)
            dpg.add_table_column(label = "Equip. ID", width_fixed=True,width=80)

            for i in range(15):
                with dpg.table_row(parent=table_green_id) as row_green_id:
                    for j in range(4):
                        if j == 0:
                            dpg.add_text(f"Player {i + 1}")
                        elif j == 1:
                            dpg.add_input_int(callback=input_id_callback, user_data=(i, j, app), on_enter=True, parent=row_green_id, step=0, step_fast=0, width = 80, tag=f"greenTable_{i}")
                        elif j == 2:
                            dpg.add_input_text(callback=input_codename_callback, user_data=(i, j, app), on_enter=True, parent=row_green_id, hint="Awaiting ID", width = 150, readonly=True, tag=f"greenTable_codename_{i}")
                        elif j == 3:
                            dpg.add_input_int(callback=input_equipID_callback, user_data=(i, j, app), on_enter=True, parent=row_green_id, step=0, step_fast=0, readonly=True, width = 80, tag=f"greenTable_equipment_{i}")

    #Red table theme
    with dpg.theme() as red_theme:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (150, 100, 100), category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (120, 120, 120), category=dpg.mvThemeCat_Core) 
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (100, 50, 50), category=dpg.mvThemeCat_Core)

    dpg.bind_item_theme(redTeam, red_theme)
    
    #Green table theme
    with dpg.theme() as green_theme:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100, 150, 100), category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (120, 120, 120), category=dpg.mvThemeCat_Core) 
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core) 
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (50, 100, 50), category=dpg.mvThemeCat_Core) 

    dpg.bind_item_theme(greenTeam, green_theme)
    
    #Pop-up for network swap
    with dpg.window(label="Switch Network", pos=(250, 250), width=300, height=100, modal=True, show=False, tag="modal_id", no_resize=True, no_move=True, no_title_bar=True):
        dpg.add_text("Input new network address, press enter:")
        dpg.add_separator()
        dpg.add_input_text(callback=network_swap_callback, on_enter=True, hint="Enter IP Address", width = 200, indent=50)
        dpg.add_button(label="Close", width=100, indent=100, callback=lambda: dpg.configure_item("modal_id", show=False))
        #add button to close window, and handling for failed IP address swap
    
    #Base window for bottom buttons
    with dpg.window(tag="Button Set", pos=(0, 410), width=900, height=200,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as buttonSet:
        with dpg.group(horizontal=True): 
            #indent determines spacing, callback determines function or pop up to call when button is pressed
            dpg.add_button(label="Switch UDP\n Network", width=100, height=100, indent=200, callback=lambda: dpg.configure_item("modal_id", show=True))
            dpg.add_button(label="Start", width=100, height=100, indent=400, callback=start_game)
            dpg.add_button(label="Clear", width=100, height=100, indent=600, callback=clear_entries)
        
    dpg.show_item("RedTable")
    dpg.show_item("GreenTable")

    # Red panel background theme for play action screen
    with dpg.theme() as red_panel_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (150, 60, 60)) 

    # Green panel background theme for play action screen
    with dpg.theme() as green_panel_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (50, 150, 50)) 

    # Play action screen window (initially hidden)
    with dpg.window(label="Play Action Screen", pos=(0, 0), width=900, height=600, show=False, tag="PlayActionScreen", no_resize=True, no_move=True):

        # Red and green team scores windows
        with dpg.group(horizontal=True):
            with dpg.child_window(width=288, height=500, tag="RedTeamScores"):
                dpg.bind_item_theme("RedTeamScores", red_panel_theme)
                dpg.add_text("Red Team Scores", color=(255,200,200), indent=70)

            # Add a new child window for current game action
            with dpg.child_window(width=288, height=500):
                dpg.add_text("Current Game Action", indent=70)

            with dpg.child_window(width=288, height=500, tag="GreenTeamScores"):
                dpg.bind_item_theme("GreenTeamScores", green_panel_theme) 
                dpg.add_text("Green Team Scores", color=(200,255,200), indent=70)


        # Game Timer window - 6 minutes per game, one time 30 second start down 
        with dpg.child_window(width=880, height=60):
            dpg.add_text("Game Timer")


# Define the countdown function
def countdown(event, pos_x, pos_y):
    root = tk.Tk()
    root.title("Countdown")
    root.attributes("-topmost", True)  # Set the window to be always on top
    root.geometry(f"+{pos_x}+{pos_y}")  # Set the position of the window
    label = tk.Label(root)
    label.pack()
    for i in reversed(range(31)):
        img = Image.open(f"countdown_images/{i}.tif")
        img = img.resize((900, 600))
        tk_img = ImageTk.PhotoImage(img)
        label.configure(image=tk_img)
        label.image = tk_img
        root.update()
        time.sleep(1)
    root.destroy()
    event.set()  # Signal that the countdown is complete


def start_game():

    #listens for hits
    hit_listener_thread = threading.Thread(target=listen_for_hits, daemon=True)
    hit_listener_thread.start()

    # Create an event to signal when the countdown is complete
    countdown_complete_event = multiprocessing.Event()

    # Retrieve the position of the Dear PyGui window
    pos_x, pos_y = dpg.get_viewport_pos()

    # Start the countdown in a separate process
    countdown_process = multiprocessing.Process(target=countdown, args=(countdown_complete_event, pos_x, pos_y))
    countdown_process.start()

    # Wait for the countdown to complete
    countdown_complete_event.wait()

    # Show the play action screen window, code for it should be directly above this function
    dpg.configure_item("PlayActionScreen", show=True)

    # Display the player codenames and scores on the play action screen using tables
    with dpg.table(header_row=False, parent="RedTeamScores"):
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        for i, codename in player_codenames["red"].items(): # Iterate through the red team player_codenames dictionary
            with dpg.table_row():
                dpg.add_text(f"{codename}") # Display the codename
                dpg.add_spacer() # spacer column 
                dpg.add_text(f"{player_scores['red'][i]}") # Display the score using player_scores dictionary

    with dpg.table(header_row=False, parent="GreenTeamScores"):
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        for i, codename in player_codenames["green"].items():
            with dpg.table_row():
                dpg.add_text(f"{codename}")
                dpg.add_spacer()
                dpg.add_text(f"{player_scores['green'][i]}")

    # Calculate and display the total scores
    total_red_score = sum(player_scores["red"].values())
    total_green_score = sum(player_scores["green"].values())

    # Add spacer to move the total score to the bottom right
    with dpg.group(horizontal=True, parent="RedTeamScores"):
        dpg.add_spacer(width=65)  
        dpg.add_text(f"Total Score: {total_red_score}", tag="RedTeamTotalScore")

    with dpg.group(horizontal=True, parent="GreenTeamScores"):
        dpg.add_spacer(width=65)  
        dpg.add_text(f"Total Score: {total_green_score}", tag="GreenTeamTotalScore")

    udpclient.send_game_code(202)
    print("Game code 202 sent")


def clear_entries():
    for i in range(15):
        # Clear red team 
        dpg.set_value(f"redTable_{i}", 0)
        dpg.set_value(f"redTable_codename_{i}", "")
        dpg.set_value(f"redTable_equipment_{i}", 0)

        # Clear green team
        dpg.set_value(f"greenTable_{i}", 0)
        dpg.set_value(f"greenTable_codename_{i}", "")
        dpg.set_value(f"greenTable_equipment_{i}", 0)

    # Clear player codenames and scores
    player_codenames["red"].clear()
    player_codenames["green"].clear()
    player_scores["red"].clear()
    player_scores["green"].clear()
    


def main():
    # Start the UDP server in a separate thread
    #udp_server_thread = threading.Thread(target=start_udp_server, daemon=True)
    #udp_server_thread.start()

    #init graphics
    dpg.create_context()
    dpg.create_viewport(title='Laser Tag', width=910, height=610)

    #splash image
    with dpg.texture_registry():
        width, height, channels, data = dpg.load_image("logo.jpg")
        dpg.add_static_texture(width, height, data, tag="splash_image")

    with dpg.window(tag="Splash Window", no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        dpg.add_image("splash_image", width=900, height=600)

    #finish graphics set up
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Splash Window", True)

    #splash screen duration
    splash_duration = 3  # duration in seconds
    start_time = time.time()
    
    app = PlayerDBApp()
    #app = fakeDatabase()
    
    #first, initial loop - splash screen
    while dpg.is_dearpygui_running():
        current_time = time.time()
        if current_time - start_time > splash_duration:
            #initialize main window
            show_main_window(app)
            break
        dpg.render_dearpygui_frame()

    #second, regular loop (continuously ran)
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

    dpg.destroy_context()

if __name__ == "__main__":
    main()
