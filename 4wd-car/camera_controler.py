# -*- coding = UTF-8 -*-
from steering import Steering
import time
import configparser


class Camera:
    def __init__(self):
        '''
        Read config file to init camera's parameter
        '''
        config = configparser.ConfigParser()
        config.read("config.ini")

        # Horiazonal direction control parameters
        HIntfNum = config.getint("camera", "HIntfNum")
        HInitPosition = config.getint("camera", "HInitPosition")
        HMinPosition = config.getint("camera", "HMinPosition")
        HMaxPosition = config.getint("camera", "HMaxPosition")
        HSpeed = config.getint("camera", "HSpeed")

        # Vertical direction control parameters
        VIntfNum = config.getint("camera", "VIntfNum")
        VInitPosition = config.getint("camera", "VInitPosition")
        VMinPosition = config.getint("camera", "VMinPosition")
        VMaxPosition = config.getint("camera", "VMaxPosition")
        VSpeed = config.getint("camera", "VSpeed")

        self.HCameraControl = Steering(
            HIntfNum, HInitPosition, HMinPosition, HMaxPosition, HSpeed)
        self.VCameraControl = Steering(
            VIntfNum, VInitPosition, VMinPosition, VMaxPosition, VSpeed)

    def cameraRotate(self, direction):
        '''
        This method is used to contorl the camera's rotating
        The value of parameter direction and its meaning as follow:
        HR - Turn right
        HL - Turn left
        VU - Turn upward
        VD - Turn downword
        '''
        if direction == "HL":
            self.HCameraControl.forwardRotation()
        elif direction == "HR":
            self.HCameraControl.reverseRotation()
        elif direction == "VU":
            self.VCameraControl.forwardRotation()
        elif direction == "VD":
            self.VCameraControl.reverseRotation()
        elif direction == "RESET":
            self.HCameraControl.reset()
            self.VCameraControl.reset()
        else:
            print(
                "Your input for camera direction is wrong, please input: HR, HL, VU, VD or RESET!")


if __name__ == "__main__":
    camera = Camera()
    while(True):
        direction = input("Please input direction: ")
        camera.cameraRotate(direction)
