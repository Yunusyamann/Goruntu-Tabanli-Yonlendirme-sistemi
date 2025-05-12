
import cv2
import numpy as np
import time
import serial

arduino = serial.Serial('COM11', 9600)
time.sleep(1)

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

green_threshold = 5000
box_width = 80
box_height = 80
distance_threshold = 200
last_time = time.time()

while True:
    ret, img = cap.read()
    if not ret:
        break

    height, width, _ = img.shape
    mid_x = width // 2
    cv2.line(img, (mid_x, 0), (mid_x, height), (255, 255, 255), 2)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

    green = np.zeros_like(img, np.uint8)
    green[mask > 0] = img[mask > 0]

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered = [(cv2.contourArea(cnt), cnt) for cnt in contours if cv2.contourArea(cnt) > green_threshold]
    sorted_contours = sorted(filtered, key=lambda x: x[0], reverse=True)[:2]

    a_center_x = b_center_x = None
    a_box = b_box = None

    for _, cnt in sorted_contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2

        if cx < mid_x:
            if a_center_x is None or cx < a_center_x:
                a_center_x = cx
                a_box = (cx - box_width // 2, cy - box_height // 2, box_width, box_height)
        else:
            if b_center_x is None or cx > b_center_x:
                b_center_x = cx
                b_box = (cx - box_width // 2, cy - box_height // 2, box_width, box_height)

    def draw_box(box, label):
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), 2)
        cv2.circle(img, (x + w // 2, y + h // 2), 6, (0, 0, 255), -1)
        cv2.putText(img, label, (x, y - 12), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 2, cv2.LINE_AA)

    if a_box:
        draw_box(a_box, "A")
    if b_box:
        draw_box(b_box, "B")

    command = "F"
    current_time = time.time()

    if current_time - last_time >= 0.5:
        if a_center_x is not None:
            distance_a = abs(a_center_x - mid_x)
        if b_center_x is not None:
            distance_b = abs(b_center_x - mid_x)

        if a_center_x is not None and distance_a < distance_threshold:
            command = "L"
        elif b_center_x is not None and distance_b < distance_threshold:
            command = "R"

        arduino.write(f"{command}".encode())
        last_time = current_time

    cv2.putText(img, f"Command: {command}", (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3, cv2.LINE_AA)
    cv2.imshow("Target Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
