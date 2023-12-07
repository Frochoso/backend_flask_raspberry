#activar entorno de desarrollo en bash: source env/bin/activate
#desactivar entorno de desarrollo en bash: deactivate
import RPi.GPIO as GPIO
from gpiozero import LED
import time
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
led = LED(27)
instance = dht11.DHT11(17)
result = instance.read()

time.sleep(1)  # Agrega un pequeño retraso antes de la primera lectura
while True:
    result = instance.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        print("LED turned ON")
        led.on()
        time.sleep(1)
        led.off()
        '''
    else:
        print("Error: %d" % result.error_code)
        '''
    time.sleep(2)
