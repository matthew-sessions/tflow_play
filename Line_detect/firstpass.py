import cv2
import numpy as numpy

# img = cv2.imread('img.jpg', 0)
# blur = cv2.GaussianBlur(img, (5,5), 0)
# canny = cv2.Canny(blur, 50, 150)
# cv2.imshow('res', canny)
# cv2.waitKey(5000)
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    blur = cv2.GaussianBlur(frame, (1,1), 0)
    canny = cv2.Canny(blur, 50, 150)
    cv2.imshow('res', canny)

  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()