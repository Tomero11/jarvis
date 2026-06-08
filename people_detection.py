from memory import save_event
from voice import speak
from ultralytics import YOLO
import cv2
import time
from datetime import datetime

model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

last_person_time = 0
last_cat_time = 0

COOLDOWN = 10
def save_picture(frame, object_type):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"captures/{object_type}_{timestamp}.jpg"

    cv2.imwrite(filename, frame)

    print(f"Image saved: {filename}")

while True:
    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            print(class_name)

            if class_name == "person":
                current_time = time.time()

                if current_time - last_person_time > COOLDOWN:
                    save_event("Person detected")
                    save_picture(frame, "person")
                    speak("Person detected")
                    last_person_time = current_time

            elif class_name == "cat":
                current_time = time.time()

                if current_time - last_cat_time > COOLDOWN:
                    save_event("Cat detected")
                    save_picture(frame, "cat")
                    speak("Cat detected")
                    last_cat_time = current_time

    annotated_frame = results[0].plot()

    cv2.imshow("Jarvis Person Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
