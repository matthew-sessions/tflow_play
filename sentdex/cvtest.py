import tensorflow as tf
import numpy as np
import cv2
import vlc
import time
model = model = tf.keras.models.load_model('eggfirst.model')
p = vlc.MediaPlayer('sound.mp3')


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    image = cv2.resize(gray, (100, 100))
    image = image.reshape(-1, 100, 100, 1)
    pred = model.predict([image])[0][0]
    if pred < 1:
        print('egg')
  
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()