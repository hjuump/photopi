import RPi.GPIO as GPIO

# LED 핀 번호 설정
LED1_PIN = 6
LED2_PIN = 5
LED3_PIN = 13
LED4_PIN = 19

def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1_PIN, GPIO.OUT)
    GPIO.setup(LED2_PIN, GPIO.OUT)
    GPIO.setup(LED3_PIN, GPIO.OUT)
    GPIO.setup(LED4_PIN, GPIO.OUT)

def control_leds_by_brightness(brightness):
    """조도 값에 따라 LED 제어"""
    if brightness <= 200:
        # 조도가 200 이하일 때 LED 4개 켜기
        GPIO.output(LED1_PIN, GPIO.HIGH)
        GPIO.output(LED2_PIN, GPIO.HIGH)
        GPIO.output(LED3_PIN, GPIO.HIGH)
        GPIO.output(LED4_PIN, GPIO.HIGH)
    else:
        # 조도가 200 초과일 때 LED 2개만 켜기
        GPIO.output(LED1_PIN, GPIO.HIGH)
        GPIO.output(LED2_PIN, GPIO.HIGH)
        GPIO.output(LED3_PIN, GPIO.LOW)
        GPIO.output(LED4_PIN, GPIO.LOW)
