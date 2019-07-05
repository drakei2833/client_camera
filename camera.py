import socket
from picamera import PiCamera
import datetime
import time


camera = PiCamera()
camera.resolution = (3280, 2464)
#determine resolution of final picture
camera.rotation = 180
#initiate pi camera and rotate by 180 degree

sleepTimeL = 1

date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    camera.capture("/home/pi/photobooth/"+ date + ".jpg")
    time.sleep(sleepTimeL);
#    camera.capture('/home/pi/Pictures/test2.jpg')
#    time.sleep(sleepTimeL);

