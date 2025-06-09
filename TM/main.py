from tkinter import *

is_night_mode = False
DAY_BACKGROUND_COLOR = "#E8E8E8"
NIGHT_BACKGROUND_COLOR = "#1E1E1E"
DAY_TEXT_COLOR = "black"
NIGHT_TEXT_COLOR = "#E0E0E0"
BACKGROUND_COLOR = DAY_BACKGROUND_COLOR
TEXT_COLOR = DAY_TEXT_COLOR
FONT_MAIN = ('Ariel', 40, 'italic')
FONT_SECONDARY = ('Ariel', 18, 'italic')


window = Tk()
window.title('Order Sheet Generator')
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

canvas = Canvas(width = 500, height=800, highlightthickness=0, bg= BACKGROUND_COLOR)
title_text = canvas.create_text(150, 50, text='Order Generator', font=FONT_MAIN)
product_type = canvas.create_text(75, 100, text= 'Type of product', font=FONT_SECONDARY)
quality = canvas.create_text(75, 130, text = 'Needle count', font=FONT_SECONDARY)
cylinder_type = canvas.create_text(75, 160, text='Type of cylinder', font=FONT_SECONDARY)
rib_quality = canvas.create_text(75, 190, text='Rib quality', font = FONT_SECONDARY)
number_of_packs = canvas.create_text(75, 210, text='Number of packs', font = FONT_SECONDARY)
product_number = canvas.create_text(75, 230, text='Number of pcs', font = FONT_SECONDARY)
composition = canvas.create_text(75, 260, text='What is composition', font= FONT_SECONDARY)
                             
canvas.grid(column=1, row=0)



window.mainloop()