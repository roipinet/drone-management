# -*- coding: UTF-8 -*-
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing, NavigateHome, moveTo
import olympe_deps as od
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from olympe.messages.camera import take_photo, set_camera_mode, set_photo_mode, photo_progress
from olympe.messages.gimbal import set_target
from olympe.messages.ardrone3.GPSSettings import SetHome
from PIL import Image
import math
import sys
import requests

homeLatitude = 48.87890000000001
homeLongitude = 2.3677799999999998
homeAltitude = 3.0

entranceLatitude = 48.879031563239856
entranceLongitude = 2.367685713676506
entranceAltitude = 0.9825900793075562


# Drone IP
ANAFI_IP = "10.202.0.1"
drone = olympe.Drone(ANAFI_IP)
# Get argument
destination = sys.argv[1]

def goToEntrance():
    print("Going to entrance")
    ##Go up
    drone(
    moveBy(0, 0, -5, 0)
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait()
    ##Go to entrance
    drone(
    moveTo(latitude=entranceLatitude, longitude=entranceLongitude,altitude=5, orientation_mode=0, heading=0)
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait()
    drone(
    moveTo(latitude=entranceLatitude, longitude=entranceLongitude,altitude=entranceAltitude, orientation_mode=0, heading=0)
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait()
    return


def goToHome():
    print("Going to HOME")
    drone(
    moveBy(0, 0, -5, 0)
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait()
    drone(
    moveTo(latitude=homeLatitude, longitude=homeLongitude,altitude=homeAltitude, orientation_mode=0, heading=0)
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait()
    return


def goToDestination(destination):

    if(destination == "A1"):
        goToEntrance()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()    
    elif(destination == "A2"):
        goToEntrance()
        drone(
            moveBy(0, 2.3, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "A3"):
        goToEntrance()
        drone(
            moveBy(0, 4.8, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "A4"):
        goToEntrance()
        drone(
            moveBy(0, 7.1, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "A5"):
        goToEntrance()
        drone(
            moveBy(0, 9.5, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "A6"):
        goToEntrance()
        drone(
            moveBy(0, 12, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "B1"):
        goToEntrance()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()    
    elif(destination == "B2"):
        goToEntrance()
        drone(
            moveBy(0, 2.3, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "B3"):
        goToEntrance()
        drone(
            moveBy(0, 4.8, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "B4"):
        goToEntrance()
        drone(
            moveBy(0, 7.1, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "B5"):
        goToEntrance()
        drone(
            moveBy(0, 9.5, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    elif(destination == "B6"):
        goToEntrance()
        drone(
            moveBy(0, 12, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        drone(
            moveBy(-4.93, 0, 0, 0)
                >> FlyingStateChanged(state="hovering", _timeout=5)
        ).wait()
        goToHome()
    
    return

print("Destination: " + destination)
drone.connection()
drone(
    TakeOff()
        >> FlyingStateChanged(state="hovering", _timeout=5)
).wait()
goToDestination(destination)
drone(Landing()).wait()
drone.disconnection()



        
