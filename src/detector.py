from ultralytics import YOLO

class Detector:
    def __init__(self, model_path="yolov8l.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        # return self.model(frame)
        return self.model(frame, verbose=False) # turns off logs
        
# model         desc        size        speed         accuracy
#yolov8n.pt :   nano        smallest    fastest       lowest
#yolov8s.pt :   small       small       very fast     good
#yolov8m.pt :   medium      medium      fast          better
#yolov8l.pt :   large       large       moderate      high                  (current)
#yolov8x.pt :   largest     largest     slow          highest