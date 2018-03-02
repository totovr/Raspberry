from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Rotate the camera
camera.rotation = 180
# Start the camera with and alpha value
camera.start_preview() 
# Stop after 5 seconds 
sleep(5)
camera.capture('/home/pi/Desktop/Capture_Picture/Image.jpg')
camera.stop_preview()
