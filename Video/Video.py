from picamera import PiCamera
from time import sleep

camera = PiCamera()

try:
camera.start_preview()
camera.start_recording('/home/pi/Videos/Pi_Videos/video.h264')
sleep(10)
camera.stop_recording()
finally:
camera.stop_preview()
