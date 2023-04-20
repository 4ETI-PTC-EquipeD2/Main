import os
import cv2
import time
from matplotlib import pyplot as plt

# init camera
execution_path = os.getcwd()
camera = cv2.VideoCapture(0)

while True:
    # Init and FPS process
    start_time = time.time()

    # Grab a single frame of video
    ret, frame = camera.read()

    # calculate FPS >> FPS = 1 / time to process loop
    fpsInfo = "FPS: " + str(1.0 / (time.time() - start_time)) 
    print(fpsInfo)

    cv2.putText(frame, fpsInfo, (8, 8), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    Test = cv2.QRCodeDetector().detect(frame)
    print(Test)
    if Test[0]==True:
        print("Entrée if")
        Qr = cv2.QRCodeDetector().detectAndDecodeCurved(frame)
        print(Qr)


        break

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
camera.release()
plt.figure()
plt.imshow(frame)

cv2.destroyAllWindows()