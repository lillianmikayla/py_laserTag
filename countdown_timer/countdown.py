# Countdown at start of game.

from PIL import Image, ImageTk
import tkinter as tk
import time

image_number = 0
root = tk.Tk()
root.title("Countdown")
label = tk.Label(root)
label.pack()

for i in reversed(range(31)):
    img = Image.open(f"countdown_images/{i}.tif")
    time.sleep(1)
    tk_img = ImageTk.PhotoImage(img)
    label.configure(image=tk_img)
    label.image = tk_img
    root.update()
root.destroy()

