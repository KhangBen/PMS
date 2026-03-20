import cv2
# import random
import os
from ultralytics import YOLO 

# File Path Setup : picking video file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "data", "example3.mp4")

# Load model ( use n for speed if needed )
yolo = YOLO("yolov8s.pt")

# open video
videoCap = cv2.VideoCapture(video_path)

# frame counter
frame_count = 0 # NEW


# main loop : runs until quit 
while True:
    # read frame
    ret, frame = videoCap.read()
    # if not break out of loop
    if not ret:
        break

    # skipping frames for faster video processing : processing every 3rd frame
    frame_count += 1 
    if frame_count % 3 != 0:
        continue

    # running YOLO
    results = yolo(frame)

    # loop through the results
    for result in results:
        class_names = result.names

        # loop through boxes detected
        for box in result.boxes:
            # confidence filter 
            if float(box.conf[0]) > 0.4:

                # bounding box coordinates : [x1,y1] [x2,y2] -> makes rectangle 
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                # class + confidence
                cls = int(box.cls[0])
                class_name = class_names[cls]
                conf = float(box.conf[0])

                if class_name == "car" or class_name == "truck":
                    color = (0, 255, 0); 


                # draw rectangles : (frame, start, end, color, thickness)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                # draw text 
                cv2.putText(frame,
                            f"{class_name} {conf:.2f}",
                            (x1, max(y1 - 10, 20)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            color,
                            2)

    # Show Frame : opens window
    cv2.imshow("Vehicle Detection", frame)

    # quitting the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# clean up
videoCap.release()
cv2.destroyAllWindows()

