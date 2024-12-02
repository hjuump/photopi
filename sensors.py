import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import busio
from adafruit_htu21d import HTU21D
import paho.mqtt.client as mqtt

TRIG = 20
ECHO = 16

# I2C 설정
i2c = busio.I2C(scl=3, sda=2)  # SCL: GPIO3, SDA: GPIO2
htu21d_sensor = HTU21D(i2c)

# MCP3008 설정
LIGHT_SENSOR_CHANNEL = 0
mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

def setup_sensors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

# 거리 측정 함수
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

# 온도 측정 함수
def get_temperature():
    return round(htu21d_sensor.temperature, 2)

# 습도 측정 함수
def get_humidity():
    return round(htu21d_sensor.relative_humidity, 2)

# 조도 측정 함수
def measure_brightness():
    return mcp.read_adc(LIGHT_SENSOR_CHANNEL)

# MQTT 설정
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

def publish_sensor_data():
    while True:
        brightness = measure_brightness()
        temperature = get_temperature()
        humidity = get_humidity()

        mqtt_client.publish("light", brightness)
        mqtt_client.publish("temperature", temperature)
        mqtt_client.publish("humidity", humidity)

        print(f"Published - Light: {brightness}, Temperature: {temperature}, Humidity: {humidity}%")
        time.sleep(1)

if __name__ == "__main__":
    setup_sensors()
    publish_sensor_data()