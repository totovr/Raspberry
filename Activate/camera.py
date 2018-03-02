from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Rotate the camera
camera.rotation = 180
# Start the camera
camera.start_preview()
# Stop after 10 seconds 
sleep(10)
camera.stop_preview()
