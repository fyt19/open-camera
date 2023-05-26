import cv2

import numpy as np

camera = cv2.VideoCapture(0)

# If it is 0, it uses the computer's camera

# If it is 1, it opens the camera plugged in from usb

# If it is 2, it

while True:
  
    ret,image=camera.read()
    
    cv2.imshow("name",image)
    
    if cv2.waitKey(30) & 0xFF == ord ("q"):
      
        break

camera.release()

cv2.destroyAllWindows()
