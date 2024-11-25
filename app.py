import cv2

def detect_faces(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print(f"Не удалось загрузить изображение: {image_path}")
        return

    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Загружаем предобученную модель для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Обнаруживаем лица на изображении
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Печатаем результат
    print(f"Обнаружено лиц: {len(faces)}")
    for (x, y, w, h) in faces:
        print(f"Лицо найдено в координатах: x={x}, y={y}, w={w}, h={h}")

if __name__ == "__main__":
    detect_faces('image.jpg')
