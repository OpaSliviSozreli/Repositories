import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led_pin = 17 

GPIO.setup(led_pin, GPIO.OUT)

photoresistor_pin = 6

GPIO.setup(photoresistor_pin, GPIO.IN)

try:
    while True:
        input_state = GPIO.input(photoresistor_pin)
        led_state = not input_state
        GPIO.output(led_pin, led_state)
        time.sleep(0.1) 
except KeyboardInterrupt:
    GPIO.cleanup()
