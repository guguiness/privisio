import cv2

class RostoDetector:
    def __init__(self, cascade_path='classifiers/haarcascade_frontalface_default.xml'):
        self.face_cascade = cv2.CascadeClassifier()
        if not self.face_cascade.load(cv2.samples.findFile(cascade_path)):
            print('--(!) Erro ao carregar o classificador de rosto')
            exit(0)

    def detectar(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rostos = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        detections = [('rosto', x, y, x + w, y + h) for (x, y, w, h) in rostos]
        return detections