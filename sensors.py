import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008

TRIG = 20
ECHO = 16
LIGHT_SENSOR_CHANNEL = 0

mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

def setup_sensors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def is_user_near(threshold=30):
    return get_distance() < threshold

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    distance = (pulse_end - pulse_start) * 17150
    return distance

def measure_brightness():
    return mcp.read_adc(LIGHT_SENSOR_CHANNEL)
