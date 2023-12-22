# Import package opencv
import cv2 

# Load citra yang akan dideteksi. Ganti dengan nama file citra yang akan dideteksi
img = cv2.imread('datatest/ball1.jpg') 

# Konversi citra menjadi grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Load model cascade yang sudah dibuat. Ganti dengan nama model yang sudah di-train
cascade_model = cv2.CascadeClassifier('models/ball_cascade.xml') 

# Proses deteksi
detect_rect = cascade_model.detectMultiScale(gray_img, 1.1, 9) 

# Membuat bounding box untuk setiap objek yang dideteksi
for (x, y, w, h) in detect_rect: 
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 

cv2.imshow('Detected', img) 

cv2.waitKey(0) 
