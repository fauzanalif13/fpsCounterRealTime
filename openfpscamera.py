import cv2
import numpy as np
import time
#import imutils

cap = cv2.VideoCapture(0)

#digunakan utk menyimpan waktu yg digunakan ketika last frame
prev_frame_time = 0
#digunakan utk menyimpan waktu yg digunakan ketika frame skrg
new_frame_time = 0

 #Menemukan versi Opencv
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver)  < 3 :
    #jika versi opencv dibawah versi 3 maka
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print ("FPS video ini adalah (cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else :
    #opencv yg digunakan sdh versi 3 maka
    fps = cap.get(cv2.CAP_PROP_FPS)
    print ("FPS video ini adalah (cv2.CAP_PROP_FPS) : {0}".format(fps))
    
while True:
    success, img = cap.read()
    if not success:
        break

    #menyalin data img
    imgGray = img.copy()
    imgGray = cv2.resize(imgGray, (640, 480))
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    new_frame_time = time.time()
    #menghitung fps
    fps = int(1/(new_frame_time-prev_frame_time))
    fpsShow = ("FPS live: {0} fps".format(fps))
    prev_frame_time = new_frame_time

    cv2.putText(imgGray, fpsShow, (7,40), font, 2, (255,0,0), 3)

    cv2.imshow("Video",imgGray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()