# Python code for detecting 6 colors.


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
     
    # Set range for orange color and 
	# define mask 
	orange_lower = np.array([0, 112, 134], np.uint8) 
	orange_upper = np.array([12, 227,255], np.uint8) 
	orange_mask = cv2.inRange(hsvFrame,orange_lower, orange_upper) 
    
    
    # Set range for purple color and 
	# define mask 
	purple_lower = np.array([112, 121, 89], np.uint8) 
	purple_upper = np.array([156, 150, 255], np.uint8) 
	purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)  
     
	# Set range for blue color and 
	# define mask 
	blue_lower = np.array([6, 150, 2], np.uint8) 
	blue_upper = np.array([120, 255, 255], np.uint8) 
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

    # Set range for red color and 
	# define mask 
	red_lower = np.array([136, 87, 111], np.uint8) 
	red_upper = np.array([180, 255, 255], np.uint8)  
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
	# Set range for green color and 
	# define mask 
	green_lower = np.array([25, 52, 72], np.uint8) 
	green_upper = np.array([102, 255, 255], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
	
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
 
	
	# For blue color 
	blue_mask = cv2.dilate(blue_mask, kernel) 
	res_blue= cv2.bitwise_and(Frame, Frame, 
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
   
   
   
   # For red color 
	red_mask = cv2.dilate(red_mask, kernel) 
	res_red = cv2.bitwise_and(Frame, Frame, 
								mask = red_mask) 
	
    	# Creating contour to track red color 
	red_contours, hierarchy = cv2.findContours(red_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, red_contour in enumerate(red_contours): 
		area = cv2.contourArea(red_contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(red_contour) 
			Frame = cv2.rectangle(Frame, (x, y), 
									(x + w, y + h), 
									(0, 0, 255), 2) 
			
			cv2.putText(Frame, "red Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 0, 255))	 
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
	cv2.imshow("6 color_detection", Frame) 
	if cv2.waitKey(10) & 0xFF == ord('s'): # s is for stopping.
		cam.release() 
		cv2.destroyAllWindows() 
		break