import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pin = 17  # замените на нужный вам пин для светодиода

GPIO.setup(led_pin, GPIO.OUT)
button = 13

GPIO.setup(button, GPIO.IN)

led_state = False

try:
    while True:
        if GPIO.input(button) == 1:
            led_state = not led_state
            GPIO.output(led_pin, led_state)
            time.sleep(0.2)
        else:
            time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
