from ultralytics import YOLO

class PlacaDetector:
    def __init__(self, model_path="assets/modelos/detect_2/train/weights/best.pt"):
        self.model = YOLO(model_path)

    def detectar(self, image):
        results = self.model.predict(image, conf=0.5)
        detections = []
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append(('placa', x1, y1, x2, y2))
        return detections