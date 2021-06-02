import urllib.request
import cv2
import numpy as np
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.0.103:8080/shot.jpg'
#cap=cv2.VideoCapture('/home/pi/Downloads/movie1.mp4')

while True:
    # Use urllib to get the image from the IP camera
    imgcap = urllib.request.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgcap.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    canny = cv2.Canny(gray, 215, 275)
    contours, hierarchies = cv2.findContours(canny,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)	
    cv2.drawContours(img, contours, -1, (0,255,0), 2)	
	# put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1) 

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
