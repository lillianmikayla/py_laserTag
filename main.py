import dearpygui.dearpygui as dpg
import time

#callback for ID handling, app_data = ID input
def input_int_callback(sender, app_data, user_data):
    info = str(app_data)
    print(f"Input from Row {user_data[0]}, Column {user_data[1]}: {info}")
    print(f"Sender: {sender}")
    
    #invalid theme for handling invalid input scenario
    with dpg.theme() as invalid_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background when hovered
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (255, 0, 0), category=dpg.mvThemeCat_Core)  # Red background when active
    
    #enables the codename input box to be edited
    #further modification to change info or send new codename to database here
    if (sender == f"redTable_{user_data[0]}") and (app_data > 0):
        dpg.configure_item(f"redTable_codename_{user_data[0]}", readonly=False)
        dpg.bind_item_theme(sender, 0)
    elif (sender == f"greenTable_{user_data[0]}") and (app_data > 0):
        dpg.configure_item(f"greenTable_codename_{user_data[0]}", readonly=False)
        dpg.bind_item_theme(sender, 0)
    else:
        #invalid input, change theme to red to indicate invalid input
        #could add further functionality here to send error message to user
        dpg.bind_item_theme(sender, invalid_theme) 
        dpg.set_value(sender, 0) 
    
    #userdata is row,col indicies of the cell, appdata is the actual contents
    #we can use this to send information into the database
    
    #ADD INPUT CHECKING TO ASSURE ID IS VALID!

#callback for CODENAME handling, app_data = codename input
def input_text_callback(sender, app_data, user_data):
    print(f"Input from Row {user_data[0]}, Column {user_data[1]}: {app_data}")
    print(f"Sender: {sender}")
    
    #further modification to send new codename to database here

#Callback for swapping network, app_data = IP Address input
def network_swap_callback(sender, app_data, user_data):
    print(f"Input: {app_data}")
    print(f"Sender: {sender}")
    
    #further modification to update network address here

def show_main_window():
    dpg.delete_item("Splash Window")
       
    #Red team entry table    
    with dpg.window(tag="RedTable", pos=(0, 0), width=400, height=400,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as redTeam:
        dpg.add_text("Red Team", parent=redTeam)
        with dpg.table(header_row=True, label = "Red Team") as table_red_id:

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column(label = "Player Number", width_fixed=True,width=100)
            dpg.add_table_column(label = "Player ID", width_fixed=True,width=80)
            dpg.add_table_column(label = "Player Codename")

            for i in range(13):
                with dpg.table_row(parent=table_red_id) as row_red_id:
                    for j in range(3):
                        if j == 0:
                            dpg.add_text(f"Player {i}")
                        elif j == 1:
                            dpg.add_input_int(callback=input_int_callback, user_data=(i, j), on_enter=True, parent=row_red_id, step=0, step_fast=0, width = 80, tag=f"redTable_{i}")
                        elif j == 2:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_red_id, hint="Awaiting ID", width = 150, readonly=True, tag=f"redTable_codename_{i}")

    #Green team entry table
    with dpg.window(tag="GreenTable", pos=(400, 0), width=400, height=400,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as greenTeam:
        dpg.add_text("Green Team", parent=greenTeam)
        with dpg.table(header_row=True, label = "Green Team") as table_green_id:

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column(label = "Player Number", width_fixed=True,width=100)
            dpg.add_table_column(label = "Player ID", width_fixed=True,width=80)
            dpg.add_table_column(label = "Player Codename")

            for i in range(13):
                with dpg.table_row(parent=table_green_id) as row_green_id:
                    for j in range(3):
                        if j == 0:
                            dpg.add_text(f"Player {i}")
                        elif j == 1:
                            dpg.add_input_int(callback=input_int_callback, user_data=(i, j), on_enter=True, parent=row_green_id, step=0, step_fast=0, width = 80, tag=f"greenTable_{i}")
                        elif j == 2:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_green_id, hint="Awaiting ID", width = 150, readonly=True, tag=f"greenTable_codename_{i}")

    #Red table theme
    with dpg.theme() as red_theme:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (150, 100, 100), category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (120, 120, 120), category=dpg.mvThemeCat_Core) 
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
            
        #with dpg.theme_component(dpg.mvTableHeaderRow):
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (100, 50, 50), category=dpg.mvThemeCat_Core)

    dpg.bind_item_theme(redTeam, red_theme)
    
    #Green table theme
    with dpg.theme() as green_theme:
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100, 150, 100), category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (120, 120, 120), category=dpg.mvThemeCat_Core) 
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core) 
            
        #with dpg.theme_component(dpg.mvTableHeaderRow):
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (50, 100, 50), category=dpg.mvThemeCat_Core) 

    dpg.bind_item_theme(greenTeam, green_theme)
    
    #Pop-up for network swap
    with dpg.window(label="Switch Network", pos=(250, 250), width=300, height=100, modal=True, show=False, tag="modal_id", no_resize=True, no_move=True, no_title_bar=True):
        dpg.add_text("Input new network address:")
        dpg.add_separator()
        dpg.add_input_text(callback=network_swap_callback, on_enter=True, hint="Enter IP Address", width = 200, indent=50)
        #add button to close window, and handling for failed IP address swap
    
    #Base window for bottom buttons
    with dpg.window(tag="Button Set", pos=(0, 400), width=800, height=200,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True) as buttonSet:
        #button to switch network
        dpg.add_button(label="Switch UDP\n Network", width=100, height=100, indent=350, callback=lambda: dpg.configure_item("modal_id", show=True))
        
    dpg.show_item("RedTable")
    dpg.show_item("GreenTable")

def main():
    #init graphics
    dpg.create_context()
    dpg.create_viewport(title='Laser Tag', width=800, height=600)

    #splash image
    with dpg.texture_registry():
        width, height, channels, data = dpg.load_image("logo.jpg")
        dpg.add_static_texture(width, height, data, tag="splash_image")

    with dpg.window(tag="Splash Window", no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        dpg.add_image("splash_image", width=798, height=598)

    #finish graphics set up
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Splash Window", True)

    #splash screen duration
    splash_duration = 1  # duration in seconds
    start_time = time.time()

    #first, initial loop - splash screen
    while dpg.is_dearpygui_running():
        current_time = time.time()
        if current_time - start_time > splash_duration:
            #initialize main window
            show_main_window()
            break
        dpg.render_dearpygui_frame()
        #print("im loop 1\n")

    #second, regular loop (continuously ran)
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        #print("im loop 2\n")

    dpg.destroy_context()

if __name__ == "__main__":
    main()