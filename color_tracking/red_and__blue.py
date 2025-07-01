# this is a module to detect red and blue colors with webcam 
# below  are the standard modules. the need to be installed and used in a virtual enviorment

import cv2 as cv  # link to install opencv_python: https://pypi.org/project/opencv-contrib-python/
import numpy  as np # link to install numpy: https://numpy.org/install/

cam = cv.VideoCapture(0) # use the webcam for video streaming


while True:
    _,frame = cam.read()
     # Convert to HSV  for red and blue
    hsv_red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv_blue = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

   # Define color range of red and blue
    
    min_blue  = np.array([110,50,50])
    max_blue  = np.array([130,255,255])
    
    min_red  = np.array([0,150,127])
    max_red  = np.array([178,255,255])
  
    # now set the color  ranges are set.
    blue_mask = cv.inRange(hsv_blue,min_blue,max_blue)
    red_mask = cv.inRange(hsv_red,min_red,max_red)
  
    # Create red contour.
    
    red_contours , hierachy = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) 
    if len(red_contours)  !=0:
        for red_contours in red_contours:
            if cv.contourArea(red_contours) > 500:
                x_red,y_red,h_red,w_red = cv.boundingRect(red_contours)
                cv.rectangle(frame,(x_red,y_red),(x_red+w_red,y_red+h_red),(0,85,255),6) #creates rectangle to  detects red color.
                red_text = 'RED' # create text for detecting red.
                
                cv.putText(frame, red_text, (x_red, y_red), 1,0.5, (0,255,0),1,1,  cv.LINE_AA)
     # Create blue contour.            
    blue_contours , hierachy = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) 
    if len(blue_contours)  !=0:
        for blue_contours in blue_contours:
            if cv.contourArea(blue_contours) > 500:
                x_blue,y_blue,h_blue,w_blue = cv.boundingRect(blue_contours)
                cv.rectangle(frame,(x_blue,y_blue,),(x_blue+w_blue,y_blue+h_blue),(104,50,50),8) #creates rectangle to  detects blue color.
                blue_text = 'BLUE'   # create text for detecting blue.
               
                cv.putText(frame,blue_text, (x_blue, y_blue), 1,0.5, (0,90,255),1,1,  cv.LINE_AA)
   
    cv.imshow("frame",frame)
    if cv.waitKey(10) == ord('s'): # s means stop loop.
        break
# i hope you like my code thats about it dawsatek out.    
    
    
