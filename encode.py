import face_recognition
import os
import pickle

DATA_DIR = "data"
ENCODING_FILE = "encodings.pkl"

known_encodings = []
known_names = []

print("🔄 Dang ma hoa du lieu...")

for name in os.listdir(DATA_DIR):
    person_dir = os.path.join(DATA_DIR, name)
    if not os.path.isdir(person_dir):
        continue

    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        image = face_recognition.load_image_file(img_path)
        encs = face_recognition.face_encodings(image)

        if encs:
            known_encodings.append(encs[0])
            known_names.append(name)

with open(ENCODING_FILE, "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print(f"✅ Da tao encodings cho {len(set(known_names))} nguoi")
