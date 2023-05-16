import RPi.GPIO as GPIO
from tkinter import Tk, Button

# Set up GPIO
GPIO.setmode(GPIO.BCM)
PIR_PIN = 38 # GPIO pin connected to PIR motion sensor
GPIO.setup(PIR_PIN, GPIO.IN)

# Create Tkinter window
window = Tk()
window.title("Motion Sensor Control")

# Variable to track current state
sensor_state = False

# Function to toggle sensor state
def toggle_sensor():
    global sensor_state
    if sensor_state:
        sensor_state = False
        GPIO.remove_event_detect(PIR_PIN)
        print("Motion sensor turned off")
    else:
        sensor_state = True
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING)
        print("Motion sensor turned on")

# Function to handle PIR motion detection
def motion_detected(channel):
    print("Motion detected!")

# Configure event detection
#GPIO.add_event_callback(PIR_PIN, motion_detected)

# Create GUI buttons
on_button = Button(window, text="On", command=toggle_sensor)
on_button.pack()

off_button = Button(window, text="Off", command=toggle_sensor)
off_button.pack()

# Start Tkinter event loop
window.mainloop()

# Clean up GPIO on program exit
GPIO.cleanup()