import webiopi

GPIO = webiopi.GPIO

#GPIO.setmode(GPIO.BCM)

DOOR = 4 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the door to output
    GPIO.setFunction(DOOR, GPIO.OUT)
    return

# loop function is repeatedly called by WebIOPi 
def loop():
   
   # toggle off
    if (GPIO.digitalRead(DOOR) == GPIO.HIGH):
        GPIO.digitalWrite(DOOR, GPIO.LOW)

  # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(DOOR, GPIO.LOW)
