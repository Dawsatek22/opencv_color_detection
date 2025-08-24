# Python code for color orange detection.


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


	# Set range for orange color and 
	# define mask 
	orange_lower = np.array([0, 112, 134], np.uint8) 
	orange_upper = np.array([12, 227,255], np.uint8) 
	orange_mask = cv2.inRange(hsvFrame,orange_lower, orange_upper) 

 
	
	# Morphological Transform, Dilation 
	# for purple color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	
	# For orange color 
	orange_mask = cv2.dilate(orange_mask, kernel) 
	res_orange = cv2.bitwise_and(Frame, Frame, 
								mask = orange_mask) 
	
    	# Creating contour to track orange color 
	orange_contours, hierarchy = cv2.findContours(orange_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, orange_contour in enumerate(orange_contours): 
		area = cv2.contourArea(orange_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(orange_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(22, 80,225), 2) 
			
			cv2.putText(Frame, "orange Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (22, 80,225)) 	 

 
	

			
	# Program Termination 
	cv2.imshow("orange color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break