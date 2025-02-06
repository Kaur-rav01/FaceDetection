import cv2 #import OpenCV library

#load the haar cascade classifier for face detection
haar_cascade=cv2.CascadeClassifier(r'C:\Users\DELL\Downloads\haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0) #open webcam

while True: #infinite loop to capture frames from webcam
    
    _,img=cam.read() #read frame from webcam
    
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert the img into grayscale(Haar cascade works better with grayscale images)
    
    # Detect faces in the grayscale image
    # Parameters:
    #  - 1.3: Scale factor (how much the image size is reduced at each scale)
    #  - 4: Minimum neighbors (higher value reduces false positives)
    faces=haar_cascade.detectMultiScale(grayImg,1.3,4)
    
    for(x,y,w,h) in faces: #loop through the detected faces
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #draw rectangle around the face
        
    cv2.imshow("FaceDetection",img) #display image with detected faces
    
    key=cv2.waitKey(10)# wait for key(10ms)
    
    print(key) #print the key value
    
    if key==27: # If the 'Esc' key (ASCII 27) is pressed, exit the loop
        break
   
cam.release() # Release the webcam resource after exiting the loop
cv2.destroyAllWindows() #close all OpenCV windows 