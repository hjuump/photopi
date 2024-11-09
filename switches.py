import time
import RPi.GPIO as GPIO

# 핀 설정
NEXT_BUTTON = 12
CONFIRM_BUTTON = 21

# 촬영 매수 선택 옵션 및 초기 선택 값
photo_counts = [2, 3, 4]
current_selection = 0  # 초기 선택된 매수 인덱스

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

