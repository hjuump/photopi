import cv2
import time
import os

def take_photo_series(photo_count):
    photo_paths = []
    if not os.path.exists("static/photos"):
        os.makedirs("static/photos")

    for i in range(photo_count):
        camera = cv2.VideoCapture(0)
        time.sleep(1)  # 카메라가 준비되도록 잠시 대기
        ret, frame = camera.read()
        if ret:
            photo_path = f"static/photos/photo_{int(time.time())}_{i}.jpg"
            cv2.imwrite(photo_path, frame)
            photo_paths.append(photo_path)
        camera.release()
        time.sleep(1)  # 사진 간격 조절

    return photo_paths