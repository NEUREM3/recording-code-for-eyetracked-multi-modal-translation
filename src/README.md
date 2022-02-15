The experiment can be run in the demo mode with the option --dummy (experiment.py --dummy)

In the dummy mode, when you are presented with the callibration screen, please place your mouse pointer on the black dot to complete the callibration. The experiment should then start presenting you with the other instructions. 

All the test observations are now kept under the folder "recordings". Please store your recordings there. 

To test if the web-cam tracking works, please run "web_cam.py".

To run the experiment with the "webcam-eyetracker", please edit the "webcam_mode.sh" to change your path names and then execute it. Please wait till the window with the output from the tracker loads (could take some time) and then start with the real experiment (entering name of the subject and list number). Please record the audio separately and then add the audio to the recording folder  (or modify the audio_module.py file as per yoursystem config). Also, the output from the 'web-cam tracker' (cam_record_default) gets saved into the 'experiment' folder (just like it happens with the actual eye-tracker. Please manually move it into the appropriate recordings folder.)

To test if the DSLR mode works, run the 'test_webcam_dslr.sh' script. If there are errors pertaining to the Liveview mode, change the mode of your camera any of the P,S,A,M modes. For a Nikon-3500, the mode that worked was the M (manual) mode. Please adjust the focus on your camera before-hand as close-ups focusing on the pupil tend to get blurry with incorrect focus settings. To see the output of the DSLR mode, edit the web_cam.py to  change the capture device. The devices are listed under /dev/video*. You can then run "webcam_mode.sh" to run the experiment using the DSLR.


