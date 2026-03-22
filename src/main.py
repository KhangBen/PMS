import os
import cv2

from detector import Detector
from video import VideoReader
from drawing import draw_boxes, draw_parking_spots
from parking_spots import parking_spots, is_occupied

# File Path Setup : picking video file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "..", "data", "example3.mp4")

# constructors
detector = Detector()
video = VideoReader(video_path)

# frame counter
frame_count = 0

# main loop : runs until quit
while True:
    # car coordinates
    cars = []

    # read frame
    ret, frame = video.read()
    h, w, _ = frame.shape
    # bottom half only for detection
    roi = frame[h//2:, :]

    # if not break out of loop
    if not ret:
        print("Error: video file not found")
        break

    # skipping frames for faster video processing : processing every n-th frame
    frame_count += 1
    if frame_count % 2 != 0:
        continue


    results = detector.detect(roi)

    offset_y = frame.shape[0] // 2 # fream height offset

    # getting car coordinates
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        y1 += offset_y
        y2 += offset_y
        cars.append((x1, y1, x2, y2))

        # get the center point of car
        cx = (x1 + x2) // 2
        # cy = (y1 + y2) // 2
        # getting 75% on y based on camera perspective
        cy = int(y1 + 0.75 * (y2 - y1)) 

        # getting center of each car deteciton
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 2) 
    


    frame = draw_boxes(frame, results)
    frame = draw_parking_spots(frame, parking_spots, cars, is_occupied)

    # Show Frame : opens window
    cv2.imshow("Detection", frame)

    # quitting program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# clean up
video.release()
cv2.destroyAllWindows()

# main-branch
