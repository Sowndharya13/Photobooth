import cv2
import time
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def capture_photos():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not accessible")
        return

    # 🔹 Initial delay before first photo
    time.sleep(5)

    for i in range(1, 5):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f"{OUTPUT_DIR}/photo{i}.jpg", frame)
            print(f"✅ Photo {i} captured")

        # 🔹 Wait only between photos
        if i < 4:
            time.sleep(3)

    cap.release()
    print("🎉 All photos captured")