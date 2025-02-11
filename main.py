import dearpygui.dearpygui as dpg
import time

def show_main_window():
    dpg.delete_item("Splash Window")
    with dpg.window(tag="Primary Window"):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    dpg.show_item("Primary Window")

def main():
    dpg.create_context()
    dpg.create_viewport(title='Laser Tag', width=800, height=800)

    with dpg.texture_registry():
        width, height, channels, data = dpg.load_image("chickens.png")
        dpg.add_static_texture(width, height, data, tag="splash_image")

    with dpg.window(tag="Splash Window", no_title_bar=True, no_resize=True, no_move=True, no_scrollbar=True):
        dpg.add_image("splash_image")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Splash Window", True)

    splash_duration = 3  # duration in seconds
    start_time = time.time()

    #first
    while dpg.is_dearpygui_running():
        current_time = time.time()
        if current_time - start_time > splash_duration:
            show_main_window()
            break
        dpg.render_dearpygui_frame()
        print("im loop 1\n")

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        print("im loop 2\n")

    dpg.destroy_context()

if __name__ == "__main__":
    main()