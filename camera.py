import cv2
import time
import os

def take_photo():
    # 사진을 저장할 디렉토리 생성
    if not os.path.exists("static/photos"):
        os.makedirs("static/photos")

    camera = cv2.VideoCapture(0)
    time.sleep(1)  # 카메라가 준비될 시간을 줌
    ret, frame = camera.read()
    camera.release()
    
    if ret:
        photo_path = f"static/photos/photo_{int(time.time())}.jpg"
        cv2.imwrite(photo_path, frame)
        return photo_path  # 촬영된 사진의 파일 경로 반환
    return None

