import os
import cv2
# import sys

from detector import Detector
from parking_spots import parking_spots, is_occupied
from drawing import draw_parking_spots

points = []

# constructors
detector = Detector()

# File Path Setup : picking video file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "..", "data", "example3.mp4")
output_path = os.path.join(BASE_DIR, "output.txt")

# clear file at start
open(output_path, "w").close()

def click_event(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
      print(f"{x},{y}")
      points.append((x,y))

      with open(output_path, "a") as f:
        f.write(f"({x}, {y})\n")

      if len(points) % 4 == 0:
        with open(output_path, "a") as f:
            f.write("---- new parking spot ----\n")

video = cv2.VideoCapture(video_path)


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

  for point in points:
    cv2.circle(frame, point, 5, (255, 255, 255), -1)

  offset_y = frame.shape[0] // 2 # fream height offset
      
  results = detector.detect(roi)

  # getting car coordinates
  for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    y1 += offset_y
    y2 += offset_y
    cars.append((x1, y1, x2, y2))

  # get the center point of car
  # cx = (x1 + x2) // 2
  # cy = (y1 + y2) // 2
  # getting 75% on y based on camera perspective
  # cy = int(y1 + 0.75 * (y2 - y1)) 

  # getting center of each car deteciton
  # cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 2) 

  frame = draw_parking_spots(frame, parking_spots, cars, is_occupied)

  # Show Frame : opens window
  cv2.imshow("Frame", frame)
  cv2.setMouseCallback("Frame", click_event)

  # quitting program
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  

# clean up
video.release()
cv2.destroyAllWindows()