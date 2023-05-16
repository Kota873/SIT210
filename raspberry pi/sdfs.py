import RPi.GPIO as GPIO
from tkinter import *

GPIO.setmode(GPIO.BCM)
PIR_PIN = 38
GPIO.setup(PIR_PIN, GPIO.IN)

root = Tk()
root.title("PIR Motion Sensor")

def turn_on():
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING)
    print("Motion sensor is ON")

def turn_off():
    GPIO.remove_event_detect(PIR_PIN)
    print("Motion sensor is OFF")

on_button = Button(root, text="ON", command=turn_on)
on_button.pack()

off_button = Button(root, text="OFF", command=turn_off)
off_button.pack()

root.mainloop()

GPIO.cleanup()
