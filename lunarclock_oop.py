# importing whole module
from tkinter import *
from datetime import *
from hijri_converter import convert
from PIL import ImageTk, Image, ImageSequence
import pytz
import time
import math
import pylunar
import ephem
import keyboard

class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=1366, height=100)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r''))]
        self.image = self.canvas.create_image(200,200, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

# creating tkinter window
root = Tk()
root.attributes('-fullscreen', True)
root.title('Lunar Phase Clock')
#root.geometry("1280x720+1280+720")
root.configure(bg='black')
app = App(root)
root.mainloop()
