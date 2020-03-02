#!/usr/bin/env python3
# This file does the same thing as webcam.cc, but in python...
# It is now obsolete but it is useful for prototyping.
from common.realtime import Ratekeeper
import cereal.messaging as messaging
import numpy as np
import threading
import cv2

FRAME_WIDTH, FRAME_HEIGHT = 1164, 874

def frame_function():
  cap = cv2.VideoCapture(0)
  pm = messaging.PubMaster(['frame'])

  while (True):
    ret, img = cap.read()
    
    if ret:
      img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))

      dat = messaging.new_message()
      dat.init('frame')
      dat.frame = {
        #"frameId": frame_id,
        "image": img.tostring(),
        "transform": [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
      }
    pm.send('frame', dat)
    #cv2.waitKey(50)
if __name__=="__main__":
  frame_function()

  cap.release()
  cv2.destroyAllWindows()
