from time import sleep
import os
#from picamera import PiCamera

#camera = PiCamera()

#def create_clip(clipLength: int, filename: str):
#    camera.start_recording()
#    sleep(clipLength)
#    camera.stop_recording()

def delete_clip(filename: str):
    os.remove(filename)

def new_clip():
    return "Link_to_video_clip"

def delete_clip(filename: str):
    os.remove(filename)