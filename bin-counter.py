import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24] 

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up_button_pin = 5     
down_button_pin = 6  

GPIO.setup(up_button_pin, GPIO.IN)
GPIO.setup(down_button_pin, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element)) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

try:
    while True:
        if GPIO.input(up_button_pin) > 0:
            num += 1
            if num > 255:
                num = 255 
            print(f"Число: {num} | Двоичное: {dec2bin(num)}")
            time.sleep(sleep_time)

        if GPIO.input(down_button_pin) > 0:
            num -= 1
            if num < 0:
                num = 0  # защита от отрицательных чисел
            print(f"Число: {num} | Двоичное: {dec2bin(num)}")
            time.sleep(sleep_time)
  
        bin_list = dec2bin(num)

        for i, led in enumerate(leds):
            GPIO.output(led, bin_list[i])

        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
