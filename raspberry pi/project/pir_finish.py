import RPi.GPIO as GPIO
from tkinter import Tk, Button
import time
import threading
import requests

GPIO.setwarnings(False)

# Configure the GPIO pins

PIR_PIN = 38
led_pin= 21
buzzer_pin= 31
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Initialize the GUI
root = Tk()
root.title("PIR Motion Sensor Control")

# Function to toggle the PIR sensor state
def toggle_pir_state():
    current_state = GPIO.input(PIR_PIN)
    new_state = GPIO.HIGH if current_state == GPIO.LOW else GPIO.LOW
    GPIO.output(PIR_PIN, new_state)


def pir():
    
    try:
        while True:
            global flg
            time.sleep(0.1)
            state=0
            state=GPIO.input(PIR_PIN)
            state-0
            if(state == 1): #if the pir motion sensor detect movement print detect
                # snf LED and buzzer inform users
                print("detect！")
                GPIO.output(led_pin, GPIO.HIGH)
                GPIO.output(buzzer_pin, GPIO.HIGH)
                #time.sleep( 0.1 )
                #root.after(100,turn_on)
                event_name="motion_detected"
                webhook_key="bwnV8Z2WsCCHk6jfRJVRVC"
                payload={'value1': 'Motion Detected'}
                url=f"https://maker.ifttt.com/trigger/{event_name}/with/key/{webhook_key}"
                requests.post(url, data=payload)
                
            elif(flg==False):
                print("stop pir")
                flg= True
                break
            else: # else print no detect and nothing
                print("no detect")
                GPIO.output(led_pin, GPIO.LOW)
                GPIO.output(buzzer_pin, GPIO.LOW)
                #root.after(100,turn_on)
                #$time.sleep( 0.1 )
                
            #root.update()
            #root.after(100,pir)
            #root.mainloop()
            
    except KeyboardInterrupt:
        GPIO.cleanup()

# Button callback functions
def turn_on():
    print('on')
    #GPIO.output(PIR_PIN,GPIO.HIGH)
    #GPIO.output(PIR_PIN, GPIO.HIGH)
    #GPIO.output(led_pin,GPIO.HIGH)
    thread=threading.Thread(target=pir)
    thread.start()
    #pir()


def turn_off():
    print('off')
    state=0
    global flg
    flg=False
    #root.after(1,turn_off)
    #state=GPIO.input(PIR_PIN)
    #GPIO.output(PIR_PIN, GPIO.LOW)

flg=True
# Create the buttons
on_button = Button(root, text="ON", command=turn_on)
on_button.pack()

off_button = Button(root, text="OFF", command=turn_off)
off_button.pack()

# Start the main loop
root.mainloop()
