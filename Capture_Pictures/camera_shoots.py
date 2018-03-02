from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Rotate the camera
camera.rotation = 180
# Start the camera with and alpha value
camera.start_preview() 
for i in range(5):
    # Stop after 5 seconds 
    sleep(5)
    camera.capture('/home/pi/Desktop/Capture_Pictures/Image%s.jpg' %i)
camera.stop_preview()
