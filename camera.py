import socket
from picamera import PiCamera
import time


camera = PiCamera()
camera.rotation = 180
#initiate pi camera and rotate by 180 degree

sleepTimeL = 1


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    camera.capture('/home/pi/Pictures/test1.jpg')
    time.sleep(sleepTimeL);
    camera.capture('/home/pi/Pictures/test2.jpg')
    time.sleep(sleepTimeL);

