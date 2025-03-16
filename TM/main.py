from tkinter import *

BACKGROUND_COLOR = '#E8E8E8'
TEXT_COLOR = 'black'


window = Tk()
window.title('Order Sheet Generator')
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width = 300, height=600, highlightthickness=0, bg= BACKGROUND_COLOR)
title_text = canvas.create_text(150, 50, text='Order Generator', font=('Ariel', 40, 'italic'),
                                fill=TEXT_COLOR)
canvas.grid(column=1, row=0, padx=10, pady=10)

window.mainloop()