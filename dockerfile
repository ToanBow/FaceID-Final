# Sử dụng Image đã cài sẵn dlib và face_recognition để tránh lỗi Hết RAM
FROM animcogn/face_recognition:cpu

# Cài đặt thư viện hệ thống (để chạy OpenCV mượt mà)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
# Cài đặt các thư viện phụ (Flask, Cloudinary...)
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Mở cổng 5000
EXPOSE 5000

# Lệnh chạy server
CMD ["python", "server.py"]