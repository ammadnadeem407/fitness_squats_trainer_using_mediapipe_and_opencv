import cv2
import time
import numpy as np
import mediapipe as mp
import process_module as pm


cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'H264')
# out = cv2.VideoWriter('test2.mp4', fourcc, 20.0, (640, 480))
pTime = 0
detector = pm.PoseDetection()
while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    img = detector.process(frame)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow('CAM', frame)
    # out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# out.release()
cv2.destroyAllWindows()
