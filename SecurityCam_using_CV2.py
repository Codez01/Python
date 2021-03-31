import cv2
import winsound
camera = cv2.VideoCapture(0)# the port of the camera

# camera = cv2.VideoCapture("video.mp4") to analyse a specific video in open cv2

while camera.isOpened():# while the cam is opened

    ret, frame1 = camera.read()# first frame copy of the cam / video

    ret, frame2 = camera.read()#second frame copy of the cam /video

    diff = cv2.absdiff(frame1, frame2)# it makes the moving part in the video/ cam different with colours

    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)# it makes the upper effect in gray scale

    blur = cv2.GaussianBlur(gray, (5, 5), 0)# it makes some bluring effect

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)# to get rid of the noise in the video/cam (makes the moving things looks sharper)


    dilated = cv2.dilate(thresh, None, iterations=3)#it makes the neccassary wanted things bigger


    #find moving things in a video, the things we wanna detect
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2) # it draws the border of the detected items giving it the colour green in this code

    for c in contours:
        if cv2.contourArea(c) < 5000:# detect every moving thing that is bigger than 5000(doesnt detect small things)
            continue

        x, y, w, h = cv2.boundingRect(c)# if the moving entity was somehow big it is gonna draw a rectangle around it
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)# give the rectangle the colour green and the axis

        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)# play a sound on movement

    if cv2.waitKey(10) == ord('q'): #end the video / live camera
        break
    cv2.imshow('Security Camera ', frame1) # show the specified video , cam

cv2.destroyAllWindows()
