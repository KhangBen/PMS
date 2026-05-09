import cv2

# load your image (PUT CORRECT PATH HERE)
image_path = "background.png"

img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load image")
    exit()

print(img.shape)

# store points
points = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked: ({x}, {y})")

        # store point
        points.append((x, y))

        # draw a circle on click
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

        # label it
        cv2.putText(img, str(len(points)), (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# create window
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

print("Instructions:")
print("- Left click to mark parking spots")
print("- Press 's' to save to file")
print("- Press 'q' to quit")

while True:
    cv2.imshow("Image", img)

    key = cv2.waitKey(1) & 0xFF

    # save points
    if key == ord('s'):
        with open("coordinates.txt", "w") as f:
            f.write("const positions = [\n")
            for x, y in points:
                f.write(f"    {{x: {x}, y: {y}}},\n")
            f.write("];\n")

        print("Saved to coordinates.txt")

    # quit
    if key == ord('q'):
        break

cv2.destroyAllWindows()