import os
import cv2

from detector import Detector
from video import VideoReader
from drawing import draw_boxes

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
    # read frame
    ret, frame = video.read()
<<<<<<< HEAD
    h, w, _ = frame.shape
    # bottom half only for detection
    roi = frame[h//2:, :]

=======
>>>>>>> 48ea0d1 (changes to main.py)
    # if not break out of loop
    if not ret:
        print("Error: video file not found")
        break

    # skipping frames for faster video processing : processing every n-th frame
    frame_count += 1
    if frame_count % 2 != 0:
        continue


    results = detector.detect(roi)
    frame = draw_boxes(frame, results)

    # Show Frame : opens window
    cv2.imshow("Detection", frame)

    # quitting program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# clean up
video.release()
cv2.destroyAllWindows()

<<<<<<< HEAD
# khang-branch
=======
# main-branch
>>>>>>> 48ea0d1 (changes to main.py)
