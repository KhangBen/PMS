import cv2

def draw_boxes(frame, results):
    for result in results:
        class_names = result.names

        for box in result.boxes:
            conf = float(box.conf[0])
            if conf < 0.4:
                continue

            cls = int(box.cls[0])
            class_name = class_names[cls]

            if class_name not in ["car", "truck"]:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            color = (0, 255, 0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame,
                        f"{class_name} {conf:.2f}",
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2)

    return frame