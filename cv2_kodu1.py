# Görüntü işleme
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevir

# Yüzleri tespit et
faces = objects.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Yüzlerin etrafını çizin
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Görüntüyü göster
cv2.imshow("Yüz Tespiti", frame)
