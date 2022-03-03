# importing whole module
from tkinter import *
from datetime import *
from hijri_converter import convert
from PIL import ImageTk,Image
import pytz
import time
import math
import pylunar
import ephem
import keyboard

#Set Location to Assalaam Observatory (PyLunar)
Latitude = (-7, 33, 0)
Longitude = (110, 45, 0)
latDec = pylunar.tuple_to_string(Latitude)
longDec = pylunar.tuple_to_string(Longitude)

#Set Time Zone
continent="Asia"
city="Jakarta"
region=continent+"/"+city
timezone=pytz.timezone(region)

#Define mi(mooninfo)
mi = pylunar.MoonInfo(Latitude, Longitude)

#Default Colours
BG = 'black'
FG = 'white'

# creating tkinter window
root = Tk()
root.attributes('-fullscreen', True)
root.title('Lunar Phase Clock')
#root.geometry("1280x720+1280+720")
root.configure(bg='black')

# This function is used to
# display time on the label
def time():
    global BG
    global FG
    bgcolor = BG
    fgcolor = FG
    
    #if (keyboard.is_pressed('c') and fgcolor=='white'):
    #    fgcolor = 'red'
    #elif (keyboard.is_pressed('c') and fgcolor=='red'):
    #    fgcolor = 'white'
    #Define Local Time
    local_time=datetime.now(timezone)
    string1=local_time.strftime("%H:%M")
    stringDay=local_time.strftime("%A")
    #stringDate=local_time.strftime("%d" + " " + "%B" + " " + "%Y")
    stringSec=local_time.strftime(":" + "%S")


    #Define UTC Time
    utc_time=datetime.now(pytz.utc)
    string2=utc_time.strftime("%H:%M:%S")

    #Define mi.update
    day = utc_time.day
    month = utc_time.month
    year = utc_time.year
    hour = utc_time.hour
    minute = utc_time.minute
    second = utc_time.second
    mi.update((year, month, day, hour, minute, second))

    #Call Altitude, Azimuth, Elongation Function
    altitude = round(mi.altitude(), 2)
    azimuth = round(mi.azimuth(), 2)
    elong = round(mi.elongation(), 2)
    phase = mi.phase_name()
    if phase == "NEW_MOON":
        view = "New"
        numview = 1
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/0_0.png').resize((500, 500)))
    
    if phase == "WAXING_CRESCENT":
        view = "Waxing Crescent"
        numview = 2
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/2_0.png').resize((500, 500)))
            
    if phase == "FIRST_QUARTER":
        view = "First Quarter"
        numview = 3
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/5_0.png').resize((500, 500)))
            
    if phase == "WAXING_GIBBOUS":
        view = "Waxing Gibbous"
        numview = 4
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/8_0.png').resize((500, 500)))
                
    if phase == "FULL_MOON":
        view = "Full"
        numview = 5
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/14_0.png').resize((500, 500)))
            
    if phase == "WANING_GIBBOUS":
        view = "Waning Gibbous"
        numview = 6
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/17_0.png').resize((500, 500)))
            
    if phase == "THIRD_QUARTER":
        view = "Third Quarter"
        numview = 7
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/22_0.png').resize((500, 500)))
            
    if phase == "WANING_CRESCENT":
        view = "Waning Crescent"
        numview = 8
        img = ImageTk.PhotoImage(Image.open('/home/pi/lunarphase_tkinter/26_0.png').resize((500, 500)))

    #Set Contents
    image.config(image=img)
    image.image = img
    dataPhase.config(text=view, foreground = fgcolor)
    dataAlt.config(text=altitude, foreground = fgcolor)
    dataAz.config(text=azimuth, foreground = fgcolor)
    dataEl.config(text=elong, foreground = fgcolor)
    dayDisp.config(text=stringDay, foreground = fgcolor)
    secDisp.config(text=stringSec, foreground = fgcolor)
    #greDateDisp.config(text=stringDate, foreground = fgcolor)
    #hijDateDisp.config(text=hijriDate, foreground = fgcolor)
    locTimeDisp.config(text=string1, foreground = fgcolor)
    utcTimeDisp.config(text=string2, foreground = fgcolor)
    locTimeDisp.after(100, time)

# Styling the label widget so that clock
# will look more attractive
frameDisp = Frame(root)
conDisp = Label(frameDisp, font = ('calibri', 12), background = 'black', foreground='white', text=continent,wraplength=1)
cityDisp = Label(frameDisp, font = ('calibri', 12), background = 'black', foreground='white', text=city,wraplength=1)
utcDisp = Label(frameDisp, font = ('calibri', 15), background = 'black', foreground='white',text="UTC")
dayDisp = Label(frameDisp, font = ('calibri', 55),
			background = 'black')
greDateDisp = Label(frameDisp, font = ('calibri', 30),
			background = 'black', text="placeholder")
hijDateDisp = Label(frameDisp, font = ('calibri', 30),
			background = 'black', text="placeholder2")
secDisp = Label(frameDisp, font = ('calibri', 40, 'bold'),
			background = 'black')
locTimeDisp = Label(frameDisp, font = ('calibri', 95, 'bold'),
			background = 'black')
utcTimeDisp = Label(frameDisp, font = ('calibri', 15, 'bold'),
			background = 'black')
image = Label(frameDisp, background = 'black')
labelPhase = Label(frameDisp, font = ('calibri', 40, 'bold'),
			background = 'black',
			foreground = 'white', text="Moon Phase")
labelAlt = Label(frameDisp, font = ('calibri', 40, 'bold'),
			background = 'black',
			foreground = 'white', text="Altitude")
labelAz = Label(frameDisp, font = ('calibri', 40, 'bold'),
			background = 'black',
			foreground = 'white', text="Azimuth")
labelEl = Label(frameDisp, font = ('calibri', 40, 'bold'),
			background = 'black',
			foreground = 'white', text="Elongation")
dataPhase = Label(frameDisp, font = ('calibri', 40),
			background = 'black')
dataAlt = Label(frameDisp, font = ('calibri', 40),
			background = 'black')
dataAz = Label(frameDisp, font = ('calibri', 40),
			background = 'black')
dataEl = Label(frameDisp, font = ('calibri', 40),
			background = 'black')
credit = Label(frameDisp, font = ('calibri', 10),
			background = 'black',
			foreground = 'white', text="Club Astronomi Santri Assalaam 2018/2019")
# Placing clock at the centre
# of the tkinter window
frameDisp.config(background = 'black')
frameDisp.place(relx=0.5, rely=0.5, anchor=CENTER)
conDisp.grid(row=0, column=1, rowspan=2, columnspan=1, pady=15,sticky=NE)
cityDisp.grid(row=0, column=2, rowspan=2, columnspan=1, pady=15,sticky=NW)
utcDisp.grid(row=2, column=1, rowspan=1, columnspan=2)
locTimeDisp.grid(row=0, column=2, rowspan=2, columnspan=7, sticky=NE)
utcTimeDisp.grid(row=2, column=2, rowspan=1, columnspan=7, padx=40, sticky=W)
secDisp.grid(row=0, column=9, rowspan=2, columnspan=1, sticky=W)
dayDisp.grid(row=0, column=10, rowspan=1, columnspan=6, sticky=SW)
greDateDisp.grid(row=1, column=10, rowspan=1, columnspan=6, sticky=SW)
hijDateDisp.grid(row=2, column=10, rowspan=1, columnspan=6, sticky=NW)
image.grid(row=3, column=0, rowspan=5, columnspan=8, padx=10, pady=10)
labelPhase.grid(row=3, column=8, rowspan=1, columnspan=4, sticky=SE)
dataPhase.grid(row=3, column=12, rowspan=1, columnspan=4, sticky=SW, padx=5)
labelAlt.grid(row=4, column=8, rowspan=1, columnspan=4, sticky=SE)
dataAlt.grid(row=4, column=12, rowspan=1, columnspan=4, sticky=SW, padx=5)
labelAz.grid(row=5, column=8, rowspan=1, columnspan=4, sticky=SE)
dataAz.grid(row=5, column=12, rowspan=1, columnspan=4, sticky=SW, padx=5)
labelEl.grid(row=6, column=8, rowspan=1, columnspan=4, sticky=SE)
dataEl.grid(row=6, column=12, rowspan=1, columnspan=4, sticky=SW, padx=5)
credit.grid(columnspan=16, sticky=E)
time()

mainloop()
