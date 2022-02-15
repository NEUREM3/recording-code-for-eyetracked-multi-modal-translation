DUMMYMODE = True # False for gaze contingent display, True for dummy mode (using mouse or joystick)


# DISPLAY
SCREENNR = 0 # number of the screen used for displaying experiment
DISPTYPE = 'psychopy' # either 'psychopy' or 'pygame'
DISPSIZE = (1920,1080) # canvas size
MOUSEVISIBLE = False # mouse visibility
BGC = (125,125,125) # backgroundcolour
FGC = (0,0,0) # foregroundcolour
FONTSIZE = 32 # font size

# INPUT
KEYLIST = ['space', 'return'] # None for all keys; list of keynames for keys of choice (e.g. ['space','9',':'] for space, 9 and ; keys)
KEYTIMEOUT = 1 # None for no timeout, or a value in milliseconds

# EYETRACKER
# general
TRACKERTYPE = 'eyelink' # either 'smi', 'eyelink' or 'dummy' (NB: if DUMMYMODE is True, trackertype will be set to dummy automatically)
SACCVELTHRESH = 35 # degrees per second, saccade velocity threshold
SACCACCTHRESH = 9500 # degrees per second, saccade acceleration threshold
# EyeLink only
# SMI only
SMIIP = '127.0.0.1'
SMISENDPORT = 4444
SMIRECEIVEPORT = 5555
