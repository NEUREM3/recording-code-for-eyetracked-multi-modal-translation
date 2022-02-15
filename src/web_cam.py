"""
WebCam GazeTracking
"""

import cv2
from gaze_tracking import GazeTracking
from datetime import datetime

def start_record(name):
    f_name = "cam_record_"+str(name)
    f = open(f_name,"a")
    f.write("left_pupil_x\tleft_pupil_y\tright_pupil_x\tright_pupil_y\ttime")

    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0) #Change it to 2 to activate the dslr mode
    while True:
        _, frame = webcam.read()
        gaze.refresh(frame)
        frame = gaze.annotated_frame()
        text = ""
        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        if left_pupil==None:
            lp = "N/A"+"\t"+"N/A"
        if left_pupil!=None:
            lp = str(left_pupil[0])+"\t"+str(left_pupil[1])
        if right_pupil==None:
            rp = "N/A"+"\t"+"N/A"
        if right_pupil!=None:
            rp = str(right_pupil[0])+"\t"+str(right_pupil[1])
        txt = lp+"\t"+rp+"\t"+str(datetime.now())+"\n"
        print(txt)
        cv2.imshow("Display", frame)
        f.write(txt)
        if cv2.waitKey(1) == 27:
            break
    
    
    f.close()
#sub = str(input("Name: "))
start_record("default")