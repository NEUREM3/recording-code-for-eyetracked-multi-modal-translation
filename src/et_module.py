#!/usr/bin/env python3
"""
This is the first version of the UFAL experiments 
to try using eye-tracking to understand 
how humans process ambiguities during translation.
"""
import os
import random
import sys
from datetime import datetime
from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.keyboard import Keyboard
from pygaze.time import Time
from pygaze.logfile import Logfile
from pygaze.eyetracker import EyeTracker
from defaults import *
import numpy as np
import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)


# import pygame # needed by pygaze anyway, to get screen size

# print to stderr; useful for debugging
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# # get screen dimensions
# screenw, screenh = pygame.display.get_surface().get_size()

from audio_module import *
from et_module import *

list_path = os.path.join(os.path.join(os.path.join(os.getcwd(),"data")),"blocks_lists")
block_path = os.path.join((os.path.join(os.path.join(os.path.join(os.getcwd(),"data")),"blocks_lists")),"blocks")


def intro_text(scr):
    """ This is the introduction string """
    scr.draw_text(text = "This is an experiment to understand how our gaze behaves during "+
    "translation.\n\nIn the next few minutes, we will first calibrate the eye-tracker\nand " +
    "then show you how the experiment will be conducted\nand what you are supposed to do."+
    "\n\nAfter the initial practice experiments, we'll move on to the real experiments."+
    "\n\nNow please:"+
    "\nAdjust your seat to see the full display (incl. the bullseye marks in corners)"+
    "\ncomfortably in the fixed frame. Do not touch the fixed frame."+
    "\nPut your hands on the keyboard (you will need just the spacebar)"+
    "\nso that you won't need to move your head to press it."+
    "\nLean your back against the chair. Sit comfortably."+
    "\nBe ready to sit still. Ideally do not change the position of your head."+
    "\n\nThank you for being a part of this!!\n\nPlease press space to continue.", fontsize = 25)
    return scr

def time_now():
    """ This gives the current time for the log file """
    return datetime.now().time()

def instructions(scr):
    """ Think about something really clever for this part as this is very important """
    scr.clear()
    scr.draw_text(text = "You will now be shown a few examples of " +
    "the tasks that you are supposed to perform.\n\n They will be " +
    "followed by the real experiments.\n"+
    "\n\n Please press spacebar to continue.", fontsize = 25)
    return scr

def instruction1_task(scr):
    """ Description of task 1 """
    scr.draw_text(text = "If you press the spacebar now, you will see an"
    " English sentence at the top of the screen. \n Your TASK 1 is to **read it aloud** "+
    "carefully! \n\n Please press spacebar after you have finished reading. ", fontsize = 25)
    return scr

def instruction1_1_task(scr):
    """ Description of task 1 """
    scr.draw_text(text = "Now comes your TASK 2: **Translate the sentence to Czech**."+
    "\n(Simply say your translation loud, for the recording.)"+
    "\n\nPlease press spacebar before you start speaking"+
    " the sentence in Czech."+
    "\nThen press spacebar after you are done speaking.", fontsize = 25)
    return scr


def instruction2_task(scr):
    """ Description of task 1 """
    scr.draw_text(text = "Great Work!! "+
    "\n\nNow comes your TASK 3: **Consider an image**."+
    "\n\nIf you press the spacebar now, an image will "+
    "appear at the bottom of the screen. You can use the information from the"+
    " image to make any modifications to the translation of the sentence."+
    "\n\n***However in certain cases, the image is not related to the sentence "+  
    "or not present at all.***"+
    "\n\nAfter looking at the image, say loudly if you'd like to modify your translation"+
    " by saying "+
    "\"I'd like to modify my translation.\" or \"I'd keep the same translation\""+
    "\nif you would like to stick with your translation."+
    "\n\nThe final TASK 4 is to **Say the translation again (modified or not)**."+
    "\nPlease press the spacebar to indicate the start of your new translation.\nYou can stop your"+
    " recording by pressing the spacebar and moving to the next sentence.", fontsize = 25)
    return scr

def callib(tracker):
    tracker.calibrate()
    tracker.drift_correction()

def ask_callib(scr,disp,tracker,kb,log):
    tracker.log("mid-experiment calibration starts")
    scr.clear()
    scr.draw_text(text= "Mid-experiment break."+
    "\n\nNow you can take a break or your instructor may need to re-calibrate the eye tracker"+
    "\n\nOnce you and everything are ready for the next sentence, press spacebar to continue ", fontsize=20)
    disp.fill(scr)
    t_0 = disp.show()
    log.write(["mid-experiment calibration starts", time_now(), t_0])
    resp, t_1 = kb.get_key()
    if resp=='return':
        tracker.stop_recording()
        callib(tracker)
        tracker.start_recording()
    tracker.log("mid-experiment calibration ends")
    tracker.log("mid-experiment calibration ends")
    log.write(["mid-experiment calibration ends", time_now(), t_1])

def task(tracker,dest,img_path,image_name,text_pres,scr,disp,log,kb_obj,kb_chc):
    """ This is the actual task """
    beep(1)
    log.write(["target text presented", time_now()])
    tracker.log("target text presented")
    scr.clear()
    #disp.fill(instruction1_1_task(scr))
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_obj.get_key()
    beep(2)
    log.write(["start response recording", time_now(), t_1])
    tracker.log(["start response recording"])
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    #scr.draw_text(text= "recording...please press spacebar to finish recording.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_obj.get_key()
    log.write(["end response recording", time_now(), t_1])
    tracker.log(["end response recording"])
    beep(2)
    log.write(["present image", time_now()])
    tracker.log("present image")
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    scr.draw_text(text= "Please press spacebar to start recording your new translation", fontsize=20)
    scr.draw_image(os.path.join(img_path,image_name),pos=(650,820))
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_chc.get_key()
    beep(2)
    if response=='return':
        log.write(["Modified translation", time_now(), t_1])
        tracker.log("Modified Translation")
    else:
        log.write(["Kept the same translation", time_now(), t_1])
        tracker.log("Kept the same translation")
         
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    #scr.draw_text(text= "recording...press spacebar to finish recording.", fontsize=20)
    scr.draw_image(os.path.join(img_path,image_name),pos=(650,820))
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()
    beep(2)
    log.write(["end response recording", time_now(), t_1])
    tracker.log("end response recording")
    beep(1)
    fixation(scr,disp)


def exp1(tracker,dest,img_path,image_name,text_pres,scr,disp,log,kb_obj,kb_chc):
    """ This is the example section"""
    beep(1)
    tracker.log("instruction-1 starts")
    scr.clear()
    disp.fill(instruction1_task(scr))
    _ = disp.show()
    _, t_1 = kb_obj.get_key()
    beep(1)
    log.write(["instruction-1 ends", time_now(), t_1])
    tracker.log("instruction-1 ends")
    

    log.write(["target text presented", time_now()])
    tracker.log("target text presented")
    scr.clear()
    disp.fill(instruction1_1_task(scr))
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    #eprint("SHOWING: ", text_pres)
    #disp.fill(scr)
    #t_0=disp.show()
    #log.write(["present_text", time_now(),t_0])
    #log.write(["start response recording", time_now()])

    #tracker.log("target text translation")
    #scr.draw_text(text = text_pres, fontsize=30, pos=(620,200))
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_obj.get_key()
    beep(2)
    log.write(["start response recording", time_now(), t_1])
    tracker.log(["start response recording"])
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    scr.draw_text(text= "Recording... Please press spacebar to indicate you are done.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_obj.get_key()
    log.write(["end response recording", time_now(), t_1])
    tracker.log(["end response recording"])
    beep(2)

    log.write(["instruction-2 starts", time_now()])
    tracker.log("instruction-2 starts")
    scr.clear()
    disp.fill(instruction2_task(scr))
    _ = disp.show()
    _, t_1 = kb_obj.get_key()
    beep(1)
    log.write(["instruction-2 ends", time_now(), t_1])
    tracker.log("instruction-2 ends")
    
    log.write(["present image", time_now()])
    tracker.log("present image")
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    scr.draw_text(text= "Please press spacebar before you start saying loudly your new translation", fontsize=20)
    scr.draw_image(os.path.join(img_path,image_name),pos=(650,820))
    disp.fill(scr)
    _ =disp.show()
    response, t_1 = kb_chc.get_key()
    beep(2)
    if response=='return':
        log.write(["Modified translation", time_now(), t_1])
        tracker.log("Modified Translation")
    else:
        log.write(["Kept the same translation", time_now(), t_1])
        tracker.log("Kept the same translation")
         
    scr.clear()
    scr.draw_text(text = text_pres, fontsize=28, pos=(620,200))
    scr.draw_text(text= "Recording... Please press spacebar to indicate you are done.", fontsize=20)
    scr.draw_image(os.path.join(img_path,image_name),pos=(650,820))
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()
    beep(2)
    log.write(["end response recording", time_now(), t_1])
    tracker.log("end response recording")
    beep(1)
    fixation(scr,disp)

def fixation(scr,disp):
    """ Describe Fixation """
    scr.clear()
    scr.draw_fixation(fixtype='cross',pw=3)
    disp.fill(scr)
    disp.show()
    Time.pause(random.randint(1000, 2000))
    scr.clear()

def example(tracker,img_path,dest,scr,disp,log,kb_obj,kb_chc):
    """ Describe Demonstration Example """

    txt_task = ("Scientist at work in a laboratory.")
    img_name = "scientist.jpg"
    exp1(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb_chc)

    scr.clear()
    scr.draw_text(text= "Great work! Here's another example sentence. Press spacebar to continue.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()    
    beep(1)


    txt_task = ("Man playing with a dog.")
    img_name = "man_dog.jpg"
    exp1(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb_chc)

    scr.clear()
    scr.draw_text(text= "Great work! This time, without the written instructions. Feel free to ask any questions. Press spacebar to continue.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()    

    txt_task = ("The phone says 'pass me the pizza'")
    img_name = "phone.jpg"
    task(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb_chc)

    scr.clear()
    beep(1)
    scr.draw_text(text= "Great work! Press spacebar to continue.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()    

    txt_task = ("Two young women are playing a game of cards.")
    img_name = "music1.jpg"
    task(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb_chc)

    scr.clear()
    beep(1)
    scr.draw_text(text= "Great work! Press spacebar to continue.", fontsize=20)
    disp.fill(scr)
    _ =disp.show()    
    response, t_1 = kb_obj.get_key()    

    txt_task = ("The president would arrive here within two hours.")
    img_name = "control.jpg"
    task(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb_chc)

def actual_exp(list,tracker,amb_img,namb_img,dest,scr,disp,log,kb_obj,kb):
    list_path= os.path.join(os.path.join(os.getcwd(),"data"),"probes")
    probe = os.path.join(list_path,"probe"+str(list))
    stimulus = open(probe,"r").read().split("\n")
    np.random.shuffle(stimulus)
    for stimuli in stimulus:
        if stimuli:
            tup = stimuli.split("\t")
            ask_callib(scr,disp,tracker,kb,log)
            exp_type = tup[0]+'_'+tup[1]
            sent_name = tup[2]
            txt_task = tup[3]
            img_name =  tup[4]
            des = exp_type+" :"+txt_task+" start"
            log.write([des,time_now()])
            t_n = "sent: "+txt_task+"begins"
            tracker.log(t_n)
            if tup[0]=="amb":
                img_path = amb_img
            elif tup[0]=="namb":
                img_path = namb_img
            task(tracker,dest,img_path,img_name,txt_task,scr,disp,log,kb_obj,kb)
            des = exp_type+" :"+txt_task+" end"
            log.write([des,time_now()])
            t_n = "sent: "+txt_task+" ends"
            tracker.log(t_n)
        tracker.log("quit option starts")
        log.write(["quit option starts", time_now()])
        scr.clear()
        scr.draw_text(text = "Please press spacebar to continue", fontsize = 25)
        disp.fill(scr)
        t_0 = disp.show()
        tracker.log("quit option shown")
        log.write(["quit option shown", time_now(), t_0])
        resp, t_1 = kb.get_key()
        if resp=='return':
            break
        else:
            continue
        tracker.log("quit option ends")
        log.write(["quit option ends", time_now()])


def main(source,lIst,args):
    """ This is the main module. Descrive stuff here """

    name = os.path.join(source,"event_file")
    e_log_name = os.path.join(source,"eye_log_file")
    e_data_name = os.path.join(source,"eye_data_file")
    ex_img = os.path.join(os.path.join(os.getcwd(),"data"),"examples")
    #ac_img = os.path.join(os.path.join(os.getcwd(),"data"),"experiment_pics")
    amb_img = os.path.join("data",os.path.join("experiment_pics","images_dr_amb"))
    namb_img = os.path.join("data",os.path.join("experiment_pics","images_dr_namb"))
    log = Logfile(filename=name)
    log.write(["probe: ", lIst])
    log.write(["event", "system_time", "time_elapsed"])
    disp = Display(disptype='psychopy',dispsize=(1920, 1080))
    scr = Screen()
    kb_obj = Keyboard(keylist=['space'])
    kb_chc = Keyboard(keylist=['space','return'])
    
    if args.dummy_run:
        tracker = EyeTracker(disp,trackertype='dummy',logfile=e_log_name,eyedatafile=e_data_name)
    else:
        tracker = EyeTracker(disp,trackertype='eyelink',logfile=e_log_name,eyedatafile=e_data_name)
    
    # ***************Actual experiment starts here**********************
    beep(6)
    start_time = time_now()
    log.write(["experiment starts", start_time, str(0)]) #Fix this ugliness
    disp.fill(intro_text(scr))
    t_0 = disp.show()
    log.write(["intro_starts", time_now(), t_0])
    _, t_1 = kb_obj.get_key()
    log.write(["intro_ends", time_now(), t_1])

    #***************Eye-Tracking Callibration***************************
    #tracker = EyeTracker(disp,trackertype='eyelink')
    if not tracker.connected():
        sys.exit("Eye-Tracker not connected. Exiting")
    #tracker.calibrate()
    #tracker.drift_correction()
    beep(1)
    callib(tracker)
    beep(1)
    l = "list"+lIst
    tracker.log("eye-tracking starts")
    tracker.start_recording()
    tracker.status_msg("eye-tracking starts")
    tracker.log("eye-tracking starts")
    log.write(["ET_calib_ends", time_now()])  

    
    # *************Instructions*******************
    
    disp.fill(instructions(scr)) 
    t_0 = disp.show()
    log.write(["example_intro_starts", time_now(), t_0])
    _, t_1 = kb_obj.get_key()
    log.write(["example_intro_ends", time_now(), t_1])
    beep(1)

    fixation(scr,disp)
    
    
    log.write(["examples_start", time_now(), t_1])
    scr.clear()
        
    tracker.log("examples start")
    example(tracker,ex_img,source,scr,disp,log,kb_obj,kb_chc)
    tracker.log("examples end")
    log.write(["examples_end", time_now()])
    
    #********************ACTUAL EXPERIMENT********************
    scr.clear()
    scr.draw_text(text = "Now the real sentences will be shown! \n"+
    "If you still have any questions, please ask them before we start."+
    "\n\n Once you are ready, Please press"
    +" spacebar to begin.", fontsize = 25)
    disp.fill(scr)
    t_0 = disp.show()
    tracker.log("rest screen starts")
    log.write(["rest_screen starts", time_now(), t_0])
    _, t_1 = kb_obj.get_key()
    tracker.log("rest screen ends")
    log.write(["rest_screen ends", time_now()])   


    actual_exp(lIst,tracker,amb_img,namb_img,source,scr,disp,log,kb_obj,kb_chc)
    
    
    
    # ******************* CLOSE ****************************
    tracker.stop_recording()
    tracker.close()
    
    scr.clear()
    scr.draw_text(text = "Thank you for participating!\n\n Please press"
    +" spacebar to end the experiment and save the results.", fontsize = 25)
    disp.fill(scr)
    _ = disp.show()
    _, t_1 = kb_obj.get_key()
    log.write(["experiment_ends", time_now(), t_1])
    log.close()
    disp.close()
    
