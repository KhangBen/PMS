import cv2
import numpy as np

# draw boxes funciton
def draw_boxes(frame, results):
    # loop through results
    for result in results:
        class_names = result.names

        # loop through the boxes detected
        for box in result.boxes:
            # confidence filter
            conf = float(box.conf[0])
            if conf < 0.15:
                continue

            # class + confidence
            cls = int(box.cls[0])
            class_name = class_names[cls]

            if class_name not in ["car", "truck"]:
                continue

            h, w, _ = frame.shape
            y_offset = h // 2

            # bounding box coordinates : [x1,y1] [x2,y2] -> makes rectangle 
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            y1 += y_offset
            y2 += y_offset

            color = (255, 255, 255)

            # # draw rectangles : (frame, start, end, color, thickness)
            # cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            # # draw text 
            # cv2.putText(frame,
            #             f"{class_name} {conf:.2f}",
            #             (x1, max(y1 - 10, 20)),
            #             cv2.FONT_HERSHEY_SIMPLEX,
            #             0.6,
            #             color,
            #             2)

    return frame

def draw_parking_spots(frame, parking_spots, cars, is_occupied):
  for spot in parking_spots:
    # convert into numpy array
    pts = np.array(spot, np.int32).reshape(-1, 1, 2)
    # reshape the array : 
    # -1 -> automatically figure out # of points
    # 1 -> required dimension for OpenCV
    # 2 -> (x,y)
    # pts = pts.reshape(-1, 1, 2)

    occupied = is_occupied(spot, cars)
    

    if occupied:
       color = (0, 0, 255)  # red
    else:
       color = (0, 255, 0) # green

    cv2.polylines(frame, [pts], True, color, 2)

  return frame


def display_spots(frame, open_spots, total_spots):
   h, w, _ = frame.shape
   cv2.putText(frame,
               f"Available Parking Spots: {open_spots}/{total_spots}",
               (w - 500, 50),
               cv2.FONT_HERSHEY_SIMPLEX,
               1,
               (0, 100, 0),
               2
               )
   return frame