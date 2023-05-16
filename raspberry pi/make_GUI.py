from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

red = LED(10)
green = LED(17)
blue = LED(12)

# Gui
win = Tk()
win.title("LED Toggleer")
myFont = tkinter.font.Font(family='Helvetica', size=36, weight='bold')

# Event function
def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"]="Turn Red on"
    else:
        red.on()
        redButton["text"]="Turn Red off"
        green.off()
        greenButton["text"]="Turn Green on"
        blue.off()
        blueButton["text"]="Turn Bule on"

def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"]="Turn Green on"
    else:
        green.on()
        greenButton["text"]="Turn Green off"
        red.off()
        redButton["text"]="Turn Red on"
        blue.off()
        blueButton["text"]="Turn Blue on"

def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"]="Turn Blue on"
    else:
        blue.on()
        blueButton["text"]="Turn Blue off"
        red.off()
        redButton["text"]="Turn Red on"
        green.off()
        greenButton["text"]="Turn Green on"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


redButton=Button(win, text='Turn Red on', font= myFont, command=redToggle, bg='bisque2', height=2, width=24)
redButton.grid(row=0, column=1)

greenButton=Button(win, text='Turn Green on', font=myFont, command=greenToggle, bg='bisque2', height=2, width=24)
greenButton.grid(row=1, column=1)

blueButton=Button(win, text='Turn Blue on', font=myFont, command=blueToggle, bg='bisque2', height=2, width=24)
blueButton.grid(row=2, column=1)

exitButton=Button(win, text='Exit', font=myFont, command=close, bg='red', height=2, width=24)
exitButton.grid(row=3, column=1)
   
        


