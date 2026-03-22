import os
import cv2
# import sys

points = []

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
  # read frame
  ret, frame = video.read()
  # if not break out of loop
  if not ret:
    print("Error: video file not found")
    break

  for point in points:
    cv2.circle(frame, point, 5, (0, 0, 255), -1)

  # Show Frame : opens window
  cv2.imshow("Frame", frame)
  cv2.setMouseCallback("Frame", click_event)

  # quitting program
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  

# clean up
video.release()
cv2.destroyAllWindows()