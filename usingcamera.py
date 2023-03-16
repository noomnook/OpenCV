import cv2
import face_recognition_models

vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()