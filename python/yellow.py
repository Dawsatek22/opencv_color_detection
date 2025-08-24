# Python code for color yellow detection.


import numpy as np 
import cv2 


# Capturing video through webcam 
cam = cv2.VideoCapture(0) 

# Start a while loop 
while(1): 
	
	# Reading the video from the 
	# webcam in image frames 
	_,Frame = cam.read() 

	# Convert the imageFrame in 
	# BGR(RGB color space) to 
	# HSV(hue-saturation-value) 
	# color space 
	hsvFrame = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV) 


	# Set range for yellow color and 
	# define mask 
	yellow_lower = np.array([30, 126, 100], np.uint8) 
	yellow_upper = np.array([34, 244, 255], np.uint8) 
	yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 

 
	
	# Morphological Transform, Dilation 
	# for purple color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	
	# For yellow color 
	yellow_mask = cv2.dilate(yellow_mask, kernel) 
	res_yellow = cv2.bitwise_and(Frame, Frame, 
								mask = yellow_mask) 
	
    	# Creating contour to track yellow color 
	yellow_contours, hierarchy = cv2.findContours(yellow_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, yellow_contour in enumerate(yellow_contours): 
		area = cv2.contourArea(yellow_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(yellow_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(33, 244, 255), 2) 
			
			cv2.putText(Frame, "yellow Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (33, 244, 255)) 	 

 
	

			
	# Program Termination 
	cv2.imshow("yellow color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break