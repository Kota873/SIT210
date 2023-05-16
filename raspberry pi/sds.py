import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 38  # Modify this pin number according to your setup

# Setup PIR motion sensor
GPIO.setup(PIR_PIN, GPIO.IN)

def toggle_pir_state():
    if GPIO.input(PIR_PIN):
        GPIO.setup(PIR_PIN, GPIO.IN)
        #pir_state_label.config(text="PIR Motion: OFF", fg="red")
        toggle_button["text"]="PIR Turn on"
    else:
        GPIO.setup(PIR_PIN, GPIO.OUT)
        #pir_state_label.config(text="PIR Motion: ON", fg="green")
        toggle_button["text"]="PIR Turn off"



# Create GUI window
window = tk.Tk()
window.title("PIR Motion Sensor Control")

# Create toggle button
toggle_button = tk.Button(window, text="PIR Turn on", command=toggle_pir_state)
toggle_button.pack(pady=10)

# Create label to display PIR motion state
pir_state_label = tk.Label(window, text="PIR Motion: OFF", fg="red", font=("Arial", 18))
pir_state_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()

# Cleanup GPIO on program exit
GPIO.cleanup()
