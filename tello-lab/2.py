""" Keyboard-controlled drone 

In this script it's shown how to control the drone with the keyboard.
After initialization we enter an infinite loop in which we read the keyboard 
state and set the drone velocities accordingly.
"""
import cv2
import get_key as kp

from djitellopy import tello 
from time import sleep

# --- Initialization
kp.init() 
drone = tello.Tello()
drone.connect()
drone.streamon()
print(f"Current battery: {drone.get_battery()}%")

def getKeyboard_input():
    """ Reads  the keyboard input and sets the velocities accordingly

    Variables set are:
        lr: left/right velocity
            modified with left/right arrow keys
        fb: forward/backward velocity
            modified with up/down arrow keys
        ud: up/down velocity
            modified with w/s keys
        yv: yaw velocity
            modified with a/d keys

    Furthermore we can press:
        e:  takeoff
        q:  land (immediatlly)
        z:  land (after 3 seconds)

    Returns
    -------
    [lr, fb, ud, yv]: list of int
        list of velocities to be set based on pressed keys
    """
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 40

    if   kp.getKey("LEFT"):  lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if   kp.getKey("UP"):    fb = speed
    elif kp.getKey("DOWN"):  fb = -speed
    
    if   kp.getKey("w"):     ud = speed
    elif kp.getKey("s"):     ud = -speed
  
    if   kp.getKey("a"):     yv = -speed
    elif kp.getKey("d"):     yv = speed
    
    if   kp.getKey("q"):     drone.land()
    if   kp.getKey("e"):     drone.takeoff()

    if kp.getKey("z"): 
        sleep(3)
        drone.land()
    return [lr, fb, ud, yv]


# --- Main loop
print("Press 'e' to takeoff")
print("Press 'q' to land")
print("Press 'z' for a lazy landing")
while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (320, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    vels = getKeyboard_input()
    drone.send_rc_control(vels[0], vels[1], vels[2], vels[3])
    sleep(0.05)
