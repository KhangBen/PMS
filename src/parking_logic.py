import cv2
import numpy as np
import time

def get_center(car):
  x1, y1, x2, y2 = car
  # get the center point of car
  cx = (x1 + x2) // 2

  # getting 75% on y based on camera perspective
  cy = int(y1 + 0.75 * (y2 - y1)) 

  return cx, cy


def is_occupied(spot, cars):
  # convert into numpy array
  pts = np.array(spot["polygon"], np.int32).reshape(-1, 1, 2)

  car_in_spot = False

  for car in cars:
    x1, y1, x2, y2 = car

    # get the center point of car
    cx = (x1 + x2) // 2
    cy = int(y1 + 0.75 * (y2 - y1))

    if cv2.pointPolygonTest(pts, (cx, cy), False) >= 0:
      car_in_spot = True
      break;
    
  # update counter
  if car_in_spot:
    spot["counter"] = min(spot["counter"] + 3, 126)
  else:
    spot["counter"] = max(spot["counter"] - 1, 0)

  # determine occupied status with threshold
  # higher = less flickering
  # lower = more sensitive
  THRESHOLD = 20

  spot["occupied"] = spot["counter"] >= THRESHOLD

  return spot["occupied"]

def count_open_spots(cars, parking_spots):
  open_spots = 0

  for spot in parking_spots:
    if not is_occupied(spot, cars):
      open_spots += 1

  return open_spots

