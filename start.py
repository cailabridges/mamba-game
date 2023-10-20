from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import pygame
import os

GAME_WIDTH = 800
GAME_HEIGHT = 600

window = Tk()
window.title("Mamba Game")
window.resizable(False, False)

# Initialize pygame mixer
pygame.mixer.init()

# Load background music
pygame.mixer.music.load("images/already.mp3")
pygame.mixer.music.set_volume(0.5)  # Adjust the volume (from 0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 means loop the music infinitely

custom_font = font.Font(family='Andora Modern Serif', size=70, weight='normal')

background_image = Image.open("images/african_safari_background.jpg")
background_image = background_image.resize(
    (GAME_WIDTH, GAME_HEIGHT), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)


def start_game():
    window.destroy()  # Close the start page window
    os.system("python main.py")  # Run the main game script


canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Draw the background image on the canvas
canvas.create_image(0, 0, anchor=NW, image=background_photo)

# Draw the text "Mamba Game" with different padding values on sides and top/bottom
title_text = "Mamba Game"
x_padding = 15  # Adjust horizontal padding
y_padding = 0  # Adjust vertical padding
text_item = canvas.create_text(
    GAME_WIDTH // 2, GAME_HEIGHT // 2, text=title_text, font=custom_font, fill='white', anchor=CENTER)

# Get the bounding box of the text
bbox = canvas.bbox(text_item)

# Create a white rectangle around the text with different padding values
padding_bbox = (bbox[0] - x_padding, bbox[1] - y_padding,
                bbox[2] + x_padding, bbox[3] + y_padding)
canvas.create_rectangle(padding_bbox, outline="white", width=2)

# Use a smaller font for the Start button
button_font = font.Font(family='Andora Modern Serif', size=20, weight='normal')

# Adjust the button position below the text
button_width = 100
button_height = 50
start_button = Button(window, text="Start", font=button_font,
                      command=start_game, bg="white")
canvas.create_window(GAME_WIDTH // 2, GAME_HEIGHT // 2 + 125,
                     window=start_button, width=button_width, height=button_height)

window_width = GAME_WIDTH
window_height = GAME_HEIGHT
x = int((window.winfo_screenwidth() / 2) - (window_width / 2))
y = int((window.winfo_screenheight() / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
