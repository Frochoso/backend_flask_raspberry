import RPi.GPIO as GPIO
import time
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(17)
result = instance.read()

while True:
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        time.sleep(2)
        result=instance.read()
    else:
        
        print("Error: %d" % result.error_code)
