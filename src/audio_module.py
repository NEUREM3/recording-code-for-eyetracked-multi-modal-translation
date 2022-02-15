#!/usr/bin/env python3
"""
This is the first version of the UFAL experiments 
to try using eye-traking to understand 
how humans process ambiguities during translation.
"""
import os
import sys
import threading
import tempfile
import queue
import sounddevice as sd
import soundfile as sf

q = queue.Queue()

class Record_Voice(object):
    def __init__(self,location):
        self.location = location
        thread = threading.Thread(target=self.run,args=())
        thread.daemon = True
        thread.start()

    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())
    
    def run(self):
        filename = tempfile.mktemp(prefix='system_recorded_audio',suffix='.wav', dir=self.location)
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x',samplerate=44100,channels=2) as file:
        #with sf.SoundFile(filename, mode='x',samplerate=44100,channels=32) as file:
            with sd.InputStream(callback=Record_Voice.callback):
                print('#' * 80)
                print('Initiated audio stream recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
        
        print('\nRecording finished: ' + repr(filename))
  