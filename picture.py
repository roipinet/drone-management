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
import os
from IPython.display import clear_output

homeLatitude = 48.87890000000001
homeLongitude = 2.3677799999999998
homeAltitude = 3.0

pictureLatitude = 48.87898296850866
pictureLongitude = 2.367688370122459
pictureAltitude = 28.323415756225586

# Drone IP
ANAFI_IP = "10.202.0.1"

# Drone web server URL
ANAFI_URL = "http://{}/".format(ANAFI_IP)

# Drone media web API URL
ANAFI_MEDIA_API_URL = ANAFI_URL + "api/v1/media/medias/"
#Connect to drone
os.system('cls' if os.name == 'nt' else 'clear')
clear_output(wait=True)
print("*******************************************************************************************************")
print("CONNECTING TO DRONE")
print("*******************************************************************************************************") 
drone = olympe.Drone(ANAFI_IP)
drone.connection()
os.system('cls' if os.name == 'nt' else 'clear')
clear_output(wait=True)
print("*******************************************************************************************************")
print("CONNECTION SUCCESSFUL")
print("*******************************************************************************************************") 
#Takeoff
os.system('cls' if os.name == 'nt' else 'clear')
clear_output(wait=True)
print("*******************************************************************************************************")
print("TAKING OFF")
print("*******************************************************************************************************") 
drone(
    TakeOff()
    >> FlyingStateChanged(state="hovering", _timeout=5)
).wait()

#Go to HOME
os.system('cls' if os.name == 'nt' else 'clear')
clear_output(wait=True)
print("*******************************************************************************************************")
print("GOING TO HOME")
print("*******************************************************************************************************") 
drone(
    moveTo(latitude=homeLatitude,longitude=homeLongitude,altitude=homeAltitude, orientation_mode=0, heading=0)
    >> FlyingStateChanged(state="hovering", _timeout=5)
).wait()
#Go to picture point
os.system('cls' if os.name == 'nt' else 'clear')
clear_output(wait=True)
print("*******************************************************************************************************")
print("GOING TO PICTURE POINT")
print("*******************************************************************************************************") 
drone(
    moveTo(latitude=pictureLatitude,longitude=pictureLongitude,altitude=pictureAltitude, orientation_mode=0, heading=0)
    >> FlyingStateChanged(state="hovering", _timeout=5)
).wait()
#Rotate camera down
print("*******************************************************************************************************")
print("AIMING CAMERA")
print("*******************************************************************************************************") 
drone(set_target(
    gimbal_id=0,
    control_mode="position",
    yaw_frame_of_reference="absolute",   # None instead of absolute
    yaw=0.0,
    pitch_frame_of_reference="absolute",
    pitch=-90.0,
    roll_frame_of_reference="absolute",     # None instead of absolute
    roll=0.0,
)).wait()
#Set camera mode
drone(
    set_camera_mode(cam_id=0, value=1)
).wait()
#Set photo mode
drone(
    set_photo_mode(cam_id=0, mode=0, format=0, file_format=0, burst=0, bracketing=0, capture_interval=0)
).wait()
# #Take picture
# drone(
#     take_photo(cam_id=0)
# ).wait()
print("*******************************************************************************************************")
print("TAKING PICTURE")
print("*******************************************************************************************************") 
photo_saved = drone(photo_progress(result="photo_saved", _policy="wait"))
drone(take_photo(cam_id=0)).wait()
photo_saved.wait()
media_id = photo_saved.received_events().last().args["media_id"]
#Go to HOME
print("*******************************************************************************************************")
print("GOING TO HOME")
print("*******************************************************************************************************") 
drone(
    moveTo(latitude=homeLatitude,longitude=homeLongitude,altitude=homeAltitude, orientation_mode=0, heading=0)
    >> FlyingStateChanged(state="hovering", _timeout=5)
).wait()
drone(Landing()).wait()
drone.disconnection()

#Save photo to local storage
print("*******************************************************************************************************")
print("SAVING PICTURE")
print("*******************************************************************************************************") 
media_info_response = requests.get(ANAFI_MEDIA_API_URL + media_id)
media_info_response.raise_for_status()
for resource in media_info_response.json()["resources"]:
        image_response = requests.get(ANAFI_URL + resource["url"])
        open('/home/rodrigo/Pictures/parkingpic.jpg', 'wb').write(image_response.content)

##Crop image
im = Image.open(r'/home/rodrigo/Pictures/parkingpic.jpg')
# Setting the points for cropped image 
left = 274
top = 2
right = 1141
bottom = 717
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
#Store cropped image 
im1.save('/home/rodrigo/Uploads/input.jpg')
print("*******************************************************************************************************")
print("PHOTO SAVED SUCCESSFULY")
print("*******************************************************************************************************") 
