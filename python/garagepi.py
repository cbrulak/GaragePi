import webiopi
import logging
import socket
from logging.handlers import SysLogHandler


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True

logger = logging.getLogger()
logger.setLevel(logging.INFO)

f = ContextFilter()
logger.addFilter(f)

syslog = SysLogHandler(address=('logsN.papertrailapp.com', 42937))
formatter = logging.Formatter('%(asctime)s %(hostname)s'
                              'YOUR_APP: %(message)s',
                              datefmt='%b %d %H:%M:%S')

syslog.setFormatter(formatter)
logger.addHandler(syslog)

logger.info("This is a message")


GPIO = webiopi.GPIO

#GPIO.setmode(GPIO.BCM)

DOOR = 4 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
    logger.info("Doing setup")
    # set the GPIO used by the door to output
    GPIO.setFunction(DOOR, GPIO.OUT)
    GPIO.digitalWrite(DOOR, GPIO.LOW)
    return

# loop function is repeatedly called by WebIOPi 
def loop():
   
   # toggle off
    if (GPIO.digitalRead(DOOR) == GPIO.HIGH):
        logger.info("turning off")
        webiopi.sleep(1)
        GPIO.digitalWrite(DOOR, GPIO.LOW)

# destroy function is called at WebIOPi shutdown
#def destroy():
    #GPIO.digitalWrite(DOOR, GPIO.LOW)
