#!/usr/bin/env python3
"""
This is the first version of the UFAL experiments 
to try using eye-traking to understand 
how humans process ambiguities during translation.
"""
import os
import sys
import argparse
from audio_module import Record_Voice
from et_module import *


parser = argparse.ArgumentParser()
parser.add_argument('--dummy', dest='dummy_run', default=False, action='store_true')
args, _ = parser.parse_known_args()
NAME= input("ID of the participant:")
NAME = os.path.join(os.path.join(os.getcwd(),"recordings"),NAME)

LIST = input("List to be presented:")
try:
    os.mkdir(str(NAME))
except FileExistsError:
    for i in range(1000):
        try:
            NAME = str(NAME)+str(i)
            os.mkdir(NAME)
            break
        except FileExistsError:
            continue

record_stuff = Record_Voice(NAME)
main(NAME,LIST,args)
print("Saved Results")

