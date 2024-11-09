from flask import Flask, render_template, redirect, url_for, jsonify
from sensors import setup_sensors, get_distance, measure_brightness
from switches import setup_switches, get_selected_photo_count, confirm_selection
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

# 앱 실행을 위한 메인 블록
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
