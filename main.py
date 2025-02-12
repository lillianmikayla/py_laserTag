import dearpygui.dearpygui as dpg
import time
    
def input_text_callback(sender, app_data, user_data):
    print(f"Input from Row {user_data[0]}, Column {user_data[1]}: {app_data}")
    #userdata is row,col indicies of the cell, appdata is the actual contents
    #we can use this to send information into the database
    
    #ADD INPUT CHECKING TO ASSURE ID IS VALID!

def show_main_window():
    dpg.delete_item("Splash Window")
        
    with dpg.window(tag="RedTable", pos=(0, 0), width=400, height=400,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        with dpg.table(header_row=True, label = "Red Team") as table_red_id:

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column(label = "Player Number")
            dpg.add_table_column(label = "Player ID")
            dpg.add_table_column(label = "Player Codename")

            for i in range(13):
                with dpg.table_row(parent=table_red_id) as row_red_id:
                    for j in range(3):
                        if j == 0:
                            dpg.add_text(f"Player {i}")
                        elif j == 1:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_red_id)
                        elif j == 2:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_red_id, hint="Awaiting ID")

    with dpg.window(tag="GreenTable", pos=(400, 0), width=400, height=400,no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        with dpg.table(header_row=True, label = "Green Team") as table_green_id:

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column(label = "Player Number")
            dpg.add_table_column(label = "Player ID")
            dpg.add_table_column(label = "Player Codename")

            for i in range(13):
                with dpg.table_row(parent=table_green_id) as row_green_id:
                    for j in range(3):
                        if j == 0:
                            dpg.add_text(f"Player {i}")
                        elif j == 1:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_green_id)
                        elif j == 2:
                            dpg.add_input_text(callback=input_text_callback, user_data=(i, j), on_enter=True, parent=row_green_id, hint="Awaiting ID")

    dpg.show_item("RedTable")
    dpg.show_item("GreenTable")

def main():
    dpg.create_context()
    dpg.create_viewport(title='Laser Tag', width=800, height=800)

    with dpg.texture_registry():
        width, height, channels, data = dpg.load_image("logo.jpg")
        dpg.add_static_texture(width, height, data, tag="splash_image")

    with dpg.window(tag="Splash Window", no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        dpg.add_image("splash_image", width=800, height=800)
        
    with dpg.theme() as global_theme:

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    dpg.bind_theme(global_theme)

    #dpg.show_style_editor()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Splash Window", True)

    splash_duration = 3  # duration in seconds
    start_time = time.time()

    #first, initial loop
    while dpg.is_dearpygui_running():
        current_time = time.time()
        if current_time - start_time > splash_duration:
            show_main_window()
            break
        dpg.render_dearpygui_frame()
        #print("im loop 1\n")

    #second, regular loop
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        #print("im loop 2\n")

    dpg.destroy_context()

if __name__ == "__main__":
    main()