import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 21 to be an input pin and set initial value to be pulled low (off)

def crashDetected():
    while True: # Run forever
        if GPIO.input(21) == GPIO.HIGH:
            print("Bit detected")
            return True
        else:
            return False
        
        #stop running file processes
        #save files to permanent directory