from ultralytics import YOLO

class Detector:
    def __init__(self, model_path="yolov8m.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        return self.model(frame)