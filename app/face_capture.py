import cv2
import os

def capture_face(student_id):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Camera not working")
        return

    while True:
        ret, frame = cam.read()

        if not ret:
            break

        cv2.imshow("Capture Face", frame)

        key = cv2.waitKey(1)

        # Press S to save
        if key == ord('s'):
            file_path = f"dataset/student_{student_id}.jpg"
            cv2.imwrite(file_path, frame)
            print("Image saved:", file_path)
            break

        # Press Q to quit
        if key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()