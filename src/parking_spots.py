import cv2
import numpy as np

# polyline drawing order : top-left -> top-right -> bottom-right -> bottom->left

parking_spots = [
  [(3, 1020), (128, 1018), (112, 1073), (11, 1067)],       # spot 1 
  [(135,1022), (362, 1012), (363, 1076), (128, 1074)],     # spot 2
  [(370,1012), (586, 999), (616, 1075), (375, 1074)],      # spot 3
  [(597, 996), (805, 980), (876, 1075), (633, 1076)],      # spot 4
  [(821, 977), (1028, 954), (1133, 1073), (894, 1074)],    # spot 5
  [(1041, 953), (1221, 932), (1400, 1075), (1153, 1074)],  # spot 6
  [(1245, 933), (1402, 909), (1589, 1050), (1432, 1075)],  # spot 7
  [(1424, 914), (1609, 894), (1817, 1018), (1603, 1043)],  # spot 8
  [(1628, 897), (1741, 888), (1915, 1001), (1833, 1017)]    # spot 9
]

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



