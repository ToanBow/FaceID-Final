import cv2
import os
import time
import face_recognition

# Cấu hình
LABEL = input('Nhap ten (label): ')
SAVE_DIR = os.path.join("data", LABEL)
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

TARGET_FRAMES = 50
i = 0

print(f"Chuan bi chup 50 anh cho: {LABEL}. Nhan 'q' de thoat.")

while i < TARGET_FRAMES:
    ret, frame = cap.read()
    if not ret: break

    # Sửa lỗi lật ảnh (Mirror Effect)
    frame = cv2.flip(frame, 1)
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)

    # Chỉ lưu ảnh khi phát hiện có khuôn mặt
    if face_locations:
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Cắt ảnh khuôn mặt và lưu
            face_img = frame[top:bottom, left:right]
            file_path = os.path.join(SAVE_DIR, f"{LABEL}_{i:03d}.jpg")
            cv2.imwrite(file_path, face_img)
        
        i += 1
        print(f"Da luu: {i}/{TARGET_FRAMES}")
        time.sleep(0.1) # Khoảng nghỉ giữa các lần chụp

    cv2.imshow("Data Collection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
print("Hoan tat thu thap du lieu.")