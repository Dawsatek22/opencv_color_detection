# Python code for color purple detection.


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


	# Set range for purple color and 
	# define mask 
	purple_lower = np.array([112, 121, 89], np.uint8) 
	purple_upper = np.array([156, 150, 255], np.uint8) 
	purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper) 

 
	
	# Morphological Transform, Dilation 
	# for purple color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	
	# For purple color 
	purple_mask = cv2.dilate(purple_mask, kernel) 
	res_purple = cv2.bitwise_and(Frame, Frame, 
								mask = purple_mask) 
	
    	# Creating contour to track purple color 
	purple_contours, hierarchy = cv2.findContours(purple_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, purple_contour in enumerate(purple_contours): 
		area = cv2.contourArea(purple_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(purple_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(112, 51, 144), 2) 
			
			cv2.putText(Frame, "purple Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (112, 51,144)) 	 

 
	

			
	# Program Termination 
	cv2.imshow("purple color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break