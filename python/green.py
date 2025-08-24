# Python code for color green detection.


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


	# Set range for green color and 
	# define mask 
	green_lower = np.array([25, 52, 72], np.uint8) 
	green_upper = np.array([102, 255, 255], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

 
	
	# Morphological Transform, Dilation 
	# for green color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	
	# For green color 
	green_mask = cv2.dilate(green_mask, kernel) 
	res_green = cv2.bitwise_and(Frame, Frame, 
								mask = green_mask) 
	
    	# Creating contour to track green color 
	green_contours, hierarchy = cv2.findContours(green_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, green_contour in enumerate(green_contours): 
		area = cv2.contourArea(green_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(green_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(0, 255, 0), 2) 
			
			cv2.putText(Frame, "Green Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 255, 0)) 	 

 
	

			
	# Program Termination 
	cv2.imshow("green color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break