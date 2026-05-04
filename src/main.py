import os
import cv2
import json
# import subprocess
import sys

from detector import Detector
from video import VideoReader
from drawing import draw_boxes, draw_parking_spots, display_spots
from parking_spots import parking_spots
from parking_logic import is_occupied, count_open_spots

# File Path Setup : picking video file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(BASE_DIR, "..", "data", "example3.mp4")

# constructors
detector = Detector()
video = VideoReader(video_path)

# frame counter
frame_count = 0

# launch dashboard script (old)
'''
dashboard_path = os.path.join(os.path.dirname(__file__), "dashboard.py")
subprocess.Popen([sys.executable, dashboard_path])
'''


# main loop : runs until quit
while True:
    # car coordinates
    cars = []

    # read frame
    ret, frame = video.read()

    # if not break out of loop
    if not ret:
        print("Error: video file not found")
        break

    h, w, _ = frame.shape
    # bottom half only for detection
    roi = frame[h//2:, :]

    # skipping frames for faster video processing : processing every 2nd frame
    frame_count += 1
    if frame_count % 2 != 0:
        continue


    results = detector.detect(roi)

    # frame height offset
    offset_y = frame.shape[0] // 2

    # getting car coordinates
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        y1 += offset_y
        y2 += offset_y

        # get class info
        cls = int(box.cls[0])
        class_name = results[0].names[cls]

        # only process cars and trucks
        if class_name in ["car", "truck"]:
            cars.append((x1, y1, x2, y2))

            # get the center point of car
            cx = (x1 + x2) // 2
            # getting 75% on y based on camera perspective
            cy = int(y1 + 0.75 * (y2 - y1)) 

            # getting point of each car deteciton
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 2) 
    
    # display drawings on frame
    frame = draw_boxes(frame, results)
    frame = draw_parking_spots(frame, parking_spots, cars, is_occupied)

    # display available spots counter
    open_spots = count_open_spots(cars, parking_spots)
    frame = display_spots(frame, open_spots, len(parking_spots))

    # Structure for data for future UI
    parking_data = {
        "system_active": True,
        "available" : open_spots,
        "total": len(parking_spots),
        "spot_statuses": [spot["occupied"] for spot in parking_spots]
    }

    # Create the path to the root directory PMS/
    

    # write this to a json file
    with open("lot_status.json", "w") as f:
        json.dump(parking_data, f)

    # debugging spot timer
    # spot_index = 19
    # print(f"Spot: {spot_index + 1} "
    #       f"counter = {parking_spots[spot_index]['counter']}, "
    #        f"occupied = {parking_spots[spot_index]['occupied']} ")


    # Show Frame : opens window
    cv2.imshow("Detection", frame)

    # quitting program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        parking_data["system_active"] = False
        with open("lot_status.json", "w") as f:
            json.dump(parking_data, f)
        break



# clean up
video.release()
cv2.destroyAllWindows()

# main-branch
