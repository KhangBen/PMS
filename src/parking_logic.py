import cv2
import numpy as np

def get_center(car):
  x1, y1, x2, y2 = car
  # get the center point of car
  cx = (x1 + x2) // 2

  # getting 75% on y based on camera perspective
  cy = int(y1 + 0.75 * (y2 - y1)) 

  return cx, cy


def is_occupied(spot, cars):
  # convert into numpy array
  pts = np.array(spot, np.int32).reshape(-1, 1, 2)

  for car in cars:
    x1, y1, x2, y2 = car

    # get the center point of car
    cx = (x1 + x2) // 2
    # cy = (y1 + y2) // 2
    cy = int(y1 + 0.75 * (y2 - y1))

    if cv2.pointPolygonTest(pts, (cx, cy), False) >= 0:
      return True
    
  # make sure return false is OUTSIDE THE for loop (wasted 40 min of trying to debug)
  # so it doesnt turn FALSE when checking other cars
  return False

def count_open_spots(cars, parking_spots):
  open_spots = 0

  for spot in parking_spots:
    if not is_occupied(spot, cars):
      open_spots += 1

  return open_spots

