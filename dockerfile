FROM python:3.9-slim

# Cài đặt các thư viện hệ thống cần thiết (Fix lỗi libgl1)
RUN apt-get update && apt-get install -y \
    build-essential cmake libopenblas-dev liblapack-dev \
    libx11-6 libgl1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Cài đặt thư viện Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port cho Streamlit (8501) và Flask (5000)
EXPOSE 8501 
EXPOSE 5000

# Lệnh khởi chạy mặc định là giao diện Web
CMD ["streamlit", "run", "web_app.py", "--server.port=8501", "--server.address=0.0.0.0"]