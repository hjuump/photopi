from flask import Flask, render_template, jsonify
from sensors import setup_sensors, get_distance, measure_brightness
from switches import setup_switches, get_selected_photo_count, confirm_selection, get_retake_option, is_long_press
from led_control import setup_leds, control_leds
from camera import take_photo_series

app = Flask(__name__)

# 초기화
setup_sensors()
setup_switches()
setup_leds()

@app.route('/')
def home():
    return render_template('index.html', message="카메라 앞에 다가가면 촬영이 시작됩니다.")

@app.route('/check_proximity')
def check_proximity():
    distance = get_distance()
    is_near = distance < 30  # 30cm 이내일 때 입장으로 간주
    return jsonify(is_near=is_near, distance=distance)

@app.route('/enter')
def enter_booth():
    brightness = measure_brightness()  # 조도 값 측정
    control_leds(brightness)  # 밝기에 따라 LED 제어
    return render_template('select_count.html', message="안녕하세요. 스위치를 이용해 촬영 매수를 선택해주세요.")

@app.route('/check_switches')
def check_switches():
    selected_count = get_selected_photo_count()  # 선택된 촬영 매수 확인
    is_confirmed = confirm_selection()  # 확인 버튼 상태 확인
    return jsonify(next=selected_count, confirm=is_confirmed)

@app.route('/start_photo')
def start_photo():
    return render_template('start_photo.html')  # 촬영 시작 템플릿

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route('/capture_photos')
def capture_photos():
    photo_count = get_selected_photo_count()
    photos = take_photo_series(photo_count)
    return render_template('display_photos.html', photos=photos)

@app.route('/select_count')
def select_count():
    return render_template('select_count.html', message="촬영 매수를 선택해 주세요.")

@app.route('/end')
def end():
    return render_template('end.html', message="이용해 주셔서 감사합니다.")

@app.route('/check_retake_switches')
def check_retake_switches():
    retake_option = get_retake_option()  # 스위치 입력값 가져오기
    is_confirmed = confirm_selection()  # 확인 버튼 확인
    print(f"Retake Option: {retake_option}, Confirmed: {is_confirmed}")  # 디버깅 로그
    return jsonify(next=retake_option, confirm=is_confirmed)

@app.route('/check_long_press')
def check_long_press():
    is_pressed = is_long_press()  # 스위치 길게 누름 확인
    return jsonify(pressed=is_pressed)

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', message="관리자 페이지에 오신 것을 환영합니다!")

@app.route('/get_sensor_data')
def get_sensor_data():
    light = measure_brightness()  # 조도 값
    temperature = get_temperature()  # 온도 값 (추가 필요)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify({
        "time": current_time,
        "light": light,
        "temperature": temperature
    })

# 앱 실행을 위한 메인 블록
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')