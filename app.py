from flask import Flask, render_template, redirect, url_for, jsonify
from sensors import setup_sensors, is_user_near, measure_brightness
from switches import setup_switches, get_selected_photo_count, confirm_selection
from led_control import setup_leds, control_leds
from camera import take_photo
import time

app = Flask(__name__)

# 초기화
setup_sensors()
setup_switches()
setup_leds()

# 전역 변수로 사진 경로 저장
photo_paths = []
current_photo_index = 0

@app.route('/')
def home():
    return render_template('index.html', message="카메라 앞에 다가가면 촬영이 시작됩니다.")

@app.route('/check_proximity')
def check_proximity():
    is_near = is_user_near()
    return jsonify(is_near=is_near)

@app.route('/enter')
def enter_booth():
    brightness = measure_brightness()
    control_leds(brightness)
    return render_template('select_count.html', message="안녕하세요. 스위치를 이용해 촬영 매수를 선택해주세요.")

@app.route('/check_switches')
def check_switches():
    selected_count = get_selected_photo_count()
    is_confirmed = confirm_selection()
    return jsonify(next=selected_count, confirm=is_confirmed)

@app.route('/start_photo')
def start_photo():
    global photo_paths, current_photo_index
    photo_paths = []  # 초기화
    current_photo_index = 0  # 첫 번째 사진부터 시작
    photo_count = get_selected_photo_count()
    return redirect(url_for('countdown_and_capture', count=photo_count))

@app.route('/countdown_and_capture/<int:count>')
def countdown_and_capture(count):
    global current_photo_index

    if current_photo_index < count:
        return render_template('countdown.html', countdown_number=3)
    else:
        return redirect(url_for('display_photos'))  # 모든 사진 촬영 완료 후 이동

@app.route('/capture_photo')
def capture_photo():
    global current_photo_index, photo_paths
    photo_path = take_photo()
    photo_paths.append(photo_path)
    current_photo_index += 1
    return redirect(url_for('countdown_and_capture', count=len(photo_paths)))  # 다음 카운트다운으로 이동

@app.route('/display_photos')
def display_photos():
    return render_template('display_photos.html', photos=photo_paths)

# 앱 실행을 위한 메인 블록
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
