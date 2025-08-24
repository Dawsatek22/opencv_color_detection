# Python code for color blue detection.


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


	# Set range for blue color and 
	# define mask 
	blue_lower = np.array([6, 150, 2], np.uint8) 
	blue_upper = np.array([120, 255, 255], np.uint8) 
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

 
	
	# Morphological Transform, Dilation 
	# for purple color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernel = np.ones((5, 5), "uint8") 
	
	
	# For green color 
	blue_mask = cv2.dilate(blue_mask, kernel) 
	res_blue = cv2.bitwise_and(Frame, Frame, 
								mask = blue_mask) 
	
    	# Creating contour to track blue color 
	blue_contours, hierarchy = cv2.findContours(blue_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, blue_contour in enumerate(blue_contours): 
		area = cv2.contourArea(blue_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(blue_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(100, 0, 0), 2) 
			
			cv2.putText(Frame, "blue Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 0, 0)) 	 

 
	

			
	# Program Termination 
	cv2.imshow("blue color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break