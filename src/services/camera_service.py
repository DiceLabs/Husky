#!/usr/bin/env python3

from multiprocessing import Process
from camera import CameraNode
from services import ServiceNames, ServicePorts
from server import start_server

class CAMERA_IDS():
    LEFT =  '207522071849'
    RIGHT = '207222072702' 

def start_camera_server(camera_id, name, port):
    camera = CameraNode(camera_id)
    start_server(name=name, port=port, callback=camera.camera_loop)

if __name__ == "__main__":
    left_process = Process(target=start_camera_server, args=(CAMERA_IDS.LEFT, ServiceNames.LEFT_CAMERA, ServicePorts[ServiceNames.LEFT_CAMERA]))
    right_process = Process(target=start_camera_server, args=(CAMERA_IDS.RIGHT, ServiceNames.RIGHT_CAMERA, ServicePorts[ServiceNames.RIGHT_CAMERA]))
    left_process.start()
    right_process.start()
    left_process.join()
    right_process.join()