import time
import RPi.GPIO as GPIO

# 핀 설정
NEXT_BUTTON = 12
CONFIRM_BUTTON = 21

LONG_PRESS_THRESHOLD = 5

# 촬영 매수 선택 옵션 및 초기 선택 값
photo_counts = [2, 3, 4]
current_selection = 0  # 초기 선택된 매수 인덱스

retake_options = [1, 2]  # 1: 다시 촬영하기, 2: 끝내기
current_retake_selection = 0

def setup_switches():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(NEXT_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(CONFIRM_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def get_selected_photo_count():
    global current_selection
    # NEXT 버튼이 눌리면 선택된 촬영 매수 변경
    if GPIO.input(NEXT_BUTTON):
        current_selection = (current_selection + 1) % len(photo_counts)
        time.sleep(0.3)  # 디바운싱을 위한 지연
    return photo_counts[current_selection]

def confirm_selection():
    # CONFIRM 버튼이 눌리면 True 반환
    if GPIO.input(CONFIRM_BUTTON):
        time.sleep(0.3)  # 디바운싱을 위한 지연
        return True
    return False

def get_retake_option():
    global current_retake_selection
    if GPIO.input(NEXT_BUTTON):  # NEXT 버튼 눌림 확인
        current_retake_selection = (current_retake_selection + 1) % len(retake_options)
        print(f"NEXT_BUTTON Pressed! Current Retake Option: {current_retake_selection}")
        time.sleep(0.3)  # 디바운싱 지연
    else:
        print("NEXT_BUTTON Not Pressed")
    return retake_options[current_retake_selection]

def is_long_press():
    start_time = None
    while GPIO.input(NEXT_BUTTON) == GPIO.HIGH:  # 버튼이 눌린 상태
        if start_time is None:
            start_time = time.time()  # 버튼이 눌리기 시작한 시간 기록
        elif time.time() - start_time >= LONG_PRESS_THRESHOLD:
            return True  # 5초 이상 눌린 경우
        time.sleep(0.1)  # 짧은 딜레이
    return False  # 버튼이 5초 이상 눌리지 않음