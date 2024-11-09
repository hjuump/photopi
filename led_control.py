import RPi.GPIO as GPIO

LED1_PIN = 6
LED2_PIN = 5

def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1_PIN, GPIO.OUT)
    GPIO.setup(LED2_PIN, GPIO.OUT)

def control_leds(led1=False, led2=False):
    GPIO.output(LED1_PIN, GPIO.HIGH if led1 else GPIO.LOW)
    GPIO.output(LED2_PIN, GPIO.HIGH if led2 else GPIO.LOW)
